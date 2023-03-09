"""Change the header information of the sac file.
"""
import os, sys
sys.path.append('./functions')
import head
from obspy import UTCDateTime, read
import torch.multiprocessing as mp
import numpy as np
##################################################params need to be modified########################################
# i/o paths
data_dir = ('./waveform_data')
event_list = sorted(os.listdir(data_dir))

# information for stations
sta_info = np.loadtxt('./input/sta_info.txt')
print('There are total %d stations.' % (sta_info.shape[0]))

# read the information of earthquake from catalog.dat
# convert to UTCDateTime and save to list
# time lat lon mag dep
f = open('./input/catalog.txt')
##################################################params need to be modified########################################

cats = f.read().splitlines()
eq_o_list = []
eq_lat_list = []
eq_lon_list = []
eq_mag_list = []
eq_dep_list = []
for cat in cats:
    eq_o = UTCDateTime(cat.split(' ')[0])
    eq_lat = cat.split(' ')[1]
    eq_lon = cat.split(' ')[2]
    eq_mag = cat.split(' ')[3]
    eq_dep = cat.split(' ')[4]

    eq_o_list.append(eq_o)
    eq_lat_list.append(eq_lat)
    eq_lon_list.append(eq_lon)
    eq_mag_list.append(eq_mag)
    eq_dep_list.append(eq_dep)
f.close()
print('There are total %d events' % (len(eq_o_list)))

if __name__ == '__main__':
    # parallel
    mp.set_start_method('spawn', force=True)
    for i in range(len(event_list)):
        # info for the ith event
        eq_o = eq_o_list[i]
        eq_lat = eq_lat_list[i]
        eq_lon = eq_lon_list[i]
        eq_mag = eq_mag_list[i]
        eq_dep = eq_dep_list[i]
        event = event_list[i]

        # directories for every event
        waveform_dir = os.path.join(data_dir, event)
        waveform_list = sorted(os.listdir(waveform_dir))

        for j in range(len(waveform_list)):
            # path for waveforms
            waveform = waveform_list[j]
            waveform_path = os.path.join(waveform_dir, waveform)
            
            # get the information of the network, station and channels and starttime
            net_id = 'AEJ'
            sta_id = waveform.split('_')[0]
            chn_id = waveform.split('_')[3].split('.')[0]

            # print(net_id, sta_id, chn_id)
            print('Change head for  %s' % (waveform_path))
                    
            # avoid the error from read
            try:
                # params for changing the begin time
                tr = read(waveform_path)[0]
                start_time = tr.stats.starttime
                b = start_time - eq_o
                
                if chn_id == 'EHN':
                    cmpaz = 0
                    cmpinc = 90
                elif chn_id == 'EHE':
                    cmpaz = 90
                    cmpinc = 90
                elif chn_id == 'EHZ':
                    cmpaz = 0
                    cmpinc = 0

                for k in range(sta_info.shape[0]):
                    if int(sta_id) == sta_info[k, 0]:
                        sta_lon = sta_info[k, 1]
                        sta_lat = sta_info[k, 2]
                        sta_el  = sta_info[k, 3]
                        # print(sta_id, sta_lon, sta_lat, sta_el)
                    else:
                        pass

                # ######################Changing Headers of file###########################
                # Changing headers for time
                time_params = {'fpath'    : waveform_path,
                            'start_time': eq_o
                            }
                head.ch_time(**time_params)

                # Changing headers for stations
                sta_params = {'fpath' : waveform_path,
                            'knetwk': net_id, 
                            'kstnm' : sta_id, 
                            'kcmpnm': chn_id, 
                            'cmpaz' : cmpaz, 
                            'cmpinc': cmpinc, 
                            'stlo'  : sta_lon,
                            'stla'  : sta_lat, 
                            'stel'  : sta_el
                            }
                head.ch_sta(**sta_params)

                # Changing headers for event
                event_params = {'fpath': waveform_path,
                                'evlo' : eq_lon, 
                                'evla' : eq_lat, 
                                'evdp' : eq_dep, 
                                'mag'  : eq_mag, 
                                'o'    : 0
                            }
                head.ch_event(**event_params)

                # Changing begintime for waveform
                event_b = {'fpath': waveform_path,
                        'b'    : b
                        }
                head.ch_b(**event_b)
            except:
                print('Bad Data')

