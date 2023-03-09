"""Copy seismic data matched the event to specified directory.
"""
import os, sys
import shutil
sys.path.append('./functions')
from obspy import read, UTCDateTime
from time_convert import dtime2int, dtime2str
import torch.multiprocessing as mp

##################################################params need to be modified########################################
# dir for raw data
raw_dir = 'G:/AEJ_raw/foldersac'
sta_list = sorted(os.listdir(raw_dir))

print("Thereare total %d stations" % (len(sta_list)))
# dir for out dat
out_dir = './waveform_data'

chns = ['EHZ', 'EHN', 'EHE']

# read the moment of earthquake from catalog.dat
# convert to UTCDateTime and save to list
f = open('./input/catalog.txt')
##################################################params need to be modified########################################

# You need to guarntee the order of eq_o_list is same to event_list(time order)
cats = f.readlines()
eq_o_list = []
for cat in cats:
    eq_o = UTCDateTime(cat.split(' ')[0])
    eq_o_list.append(eq_o)

    # make dirs for events
    mag = cat.split(' ')[3]
    str_time = dtime2str(eq_o)
    event_name = '_'.join([str_time, mag])
    event_dir = os.path.join(out_dir, event_name)
    if not os.path.exists(event_dir): os.makedirs(event_dir)
f.close()

event_list = sorted(os.listdir(out_dir))
print('There are total %d events' % (len(event_list)))

if __name__ == '__main__':
    # parallel
    mp.set_start_method('spawn', force=True)
    for i in range(len(event_list)):

        # the time for earthquake
        eq_o = eq_o_list[i]
        eq_o_int = dtime2int(eq_o)
        eq_o_day = eq_o.julday

        # the path for every event
        # also save the waveforms
        event = event_list[i]
        event_path = os.path.join(out_dir, event)

        for j in range(len(sta_list)):
            # information for station
            sta_id = sta_list[j]
            
            # waveforms path of raw data
            waveforms_dir = os.path.join(raw_dir, sta_id)
            waveforms = sorted(os.listdir(waveforms_dir))

            for k in range(len(waveforms)):
                # path for waveform
                waveform = waveforms[k]
                waveform_path = os.path.join(waveforms_dir, waveform)

                # determine the format right or not
                # prevent the error from UTCDateTime 
                try:
                    waveform_startdate = UTCDateTime(waveform[:8])
                    waveform_startday = waveform_startdate.julday
                    chn = waveform.split('.')[-2]
                    data_type = waveform.split('.')[-1]

                    # avoid the wrong waveform
                    if chn in chns and data_type == 'SAC':
                        # avoid the mistakes from bad data
                        # prevent error from read
                        try:
                            if eq_o_day == waveform_startday or (eq_o_day-1) == waveform_startday or (eq_o_day-2) == waveform_startday:
                                # read the waveform
                                st = read(waveform_path)
                                tr = st[0]

                                # starttime and endtime 
                                starttime = tr.stats.starttime
                                endtime = tr.stats.endtime
                                starttime_int = dtime2int(starttime)
                                endtime_int = dtime2int(endtime)
                                
                                # copy the waveforms which record the event
                                if eq_o_int >= starttime_int and eq_o_int <= endtime_int:

                                    # waveform path for out data
                                    out_name = sta_id + '_' + event + '_' + chn + '.' + data_type
                                    out_path = os.path.join(event_path, out_name)

                                    print(waveform_path, out_path)
                                    shutil.copy(waveform_path, out_path)
                        except:
                            print('Error in %s, %s' % (sta_id, waveform))
                except:
                    print('Bad Data!')

