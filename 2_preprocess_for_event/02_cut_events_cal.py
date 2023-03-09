"""Cut events by calculated arrival time form taup.
"""
import os, sys
sys.path.append('./functions')
from obspy import read
from obspy.taup import TauPyModel
from cut import cut
# import head
import torch.multiprocessing as mp

###################################################params need to be modified####################################
# i/o paths
data_dir = ('./waveform_data')
out_dir = ('./events_data_cal_p5+s25s')
if not os.path.exists(out_dir): os.makedirs(out_dir)

# params for cutting(unit: s)
p_before = 5
s_after = 25
# p_after = 25

# frequency range for bandpass
filter_range = filter_range = [0.5, 5]

# Data for waveform with short length to cut
data_fail = open('./output/data_fail.dat', 'w')

# Event list
event_list = sorted(os.listdir(data_dir))

# Model for calculated traveltime
model = TauPyModel(model="ak135")

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
                
                # distance in degree
                dist = tr.stats.sac['gcarc']
                eq_dep = tr.stats.sac['evdp']
                ##################################################### arrival time ##################################
                # arrivals for S wave
                p_arrivals = model.get_travel_times(source_depth_in_km=float(eq_dep), 
                                                    distance_in_degree=dist, phase_list=['P', 'Pn', 'Pg', 'p', 'Pdiff'])          
                
                # get the first arrival time of p wave
                p_arr_list = []
                for i in range(len(p_arrivals)):
                    p_t = p_arrivals[i].time
                    p_arr_list.append(p_t)

                p_arr = min(p_arr_list)

                # arrivals for S wave
                s_arrivals = model.get_travel_times(source_depth_in_km=float(eq_dep), 
                                                    distance_in_degree=dist, phase_list=['S', 'Sn', 'Sg', 's', 'Sdiff'])          
                
                # get the first arrival time of p wave
                s_arr_list = []
                for i in range(len(s_arrivals)):
                    s_t = s_arrivals[i].time
                    s_arr_list.append(s_t)

                s_arr = min(s_arr_list)
                # print(p_arr, s_arr)
                #################################################### arrival time ##################################

                # 60s before P and 300s afetr S
                eq_o = tr.stats.starttime - tr.stats.sac['b']
                t0 = eq_o + p_arr - p_before
                # t1 = eq_o + p_arr + p_after
                t1 = eq_o + s_arr + s_after

                # print(t0, t1, tr.stats.starttime, tr.stats.endtime)
                # avoid the error from cut
                try:
                    # cut the event
                    tr = cut(tr, t0, t1)

                    # Modify the start_time of the waveform
                    # In order to process the next cut
                    tr.stats.starttime = t0

                    # write the p and 
                    tr.stats.sac['user9'] = p_arr
                    tr.stats.sac['user8'] = s_arr

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
