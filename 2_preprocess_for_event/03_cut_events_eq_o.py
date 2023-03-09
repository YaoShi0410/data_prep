"""Cut events by calculated arrival time form taup.
"""
import os, sys
sys.path.append('./functions')
from obspy import read, UTCDateTime
from cut import cut
# import head
import torch.multiprocessing as mp

###################################################params need to be modified####################################
# i/o paths
data_dir = ('./events_data_0-300s')
out_dir = ('./events_data_0-60s')
if not os.path.exists(out_dir): os.makedirs(out_dir)

# params for cutting(unit: s)
before = 0
after = 60

# frequency range for bandpass
filter_range = filter_range = [1, 10]

# Data for waveform with short length to cut
data_fail = open('./output/data_fail.dat', 'w')

# Event list
event_list = sorted(os.listdir(data_dir))

###################################################params need to be modified####################################

if __name__ == '__main__':
    # parallel
    mp.set_start_method('spawn', force=True)

    for i in range(len(event_list)):
        # info for th ith event
        event = event_list[i]

        # Numbering for every event.
        event_num = 'AEJ' + str(i + 1) + '_' + event.split('_')[1]

        # directories for every event
        waveform_dir = os.path.join(data_dir, event)
        waveform_list = sorted(os.listdir(waveform_dir))

        for j in range(len(waveform_list)):
            # path for waveforms
            waveform = waveform_list[j]
            waveform_path = os.path.join(waveform_dir, waveform)
            
            # print('Cut for event: %s, and waveform: %s' % (event, waveform))
            # avoid the error from read
            try:
                st = read(waveform_path)
                tr =st[0]
                
                # 60s before P and 300s afetr S
                eq_o = tr.stats.starttime - tr.stats.sac['b']
                t0 = eq_o - before
                t1 = eq_o + after

                # print(t0, t1, tr.stats.starttime, tr.stats.endtime)
                # avoid the error from cut
                try:
                    # cut the event
                    tr = cut(tr, t0, t1)

                    # Modify the start_time of the waveform
                    # In order to process the next cut
                    tr.stats.starttime = t0

                    # preprocess
                    tr.detrend("demean") # rmean
                    tr.detrend("linear") # rtrend
                    tr.taper(max_percentage = 0.05, type = 'cosine') # taper
                    # tr.filter('bandpass', freqmin = filter_range[0], freqmax = filter_range[1], zerophase = True) # filter

                    # define the output dir and name
                    data_event_dir = os.path.join(out_dir, event_num)
                    if not os.path.exists(data_event_dir): os.makedirs(data_event_dir)
                    data_event_path = os.path.join(data_event_dir, waveform)

                    print(data_event_path)
                    tr.write(data_event_path, format='SAC')
                except:
                    print('Bad length for %s, %s\n' % (event, waveform))
                    data_fail.write('Bad length for %s, %s\n' % (event, waveform))
            except:
                print('Bad Data!')
            
data_fail.close()
