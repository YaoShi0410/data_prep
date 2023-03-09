"""Merge data and cut into specific length.
"""
import os, glob, sys
sys.path.append('./functions')
from obspy import read, UTCDateTime, Stream
import numpy as np
from cut import cut
from time_convert import dtime2eqt
import torch.multiprocessing as mp

##################################################params need to be modified########################################
# i/o paths
data_dir = 'G:/AEJ_raw/foldersac'
out_data_dir = 'H:/AEJ_data_day'

sta_info = np.loadtxt('./input/sta_info.txt')

# Time of record
start_time = UTCDateTime('2021-09-17T00:00:00.000000Z')
end_time = UTCDateTime('2021-11-27T00:00:00.000000Z')
num_days = int((end_time - start_time) / 86400) 
print('There are total %d days.' % (num_days))

sta_list = os.listdir(data_dir)
print('There are total %d stations.' % (len(sta_list)))

net = 'AEJ'
location = '00'

chns = ['EHE', 'EHN', 'EHZ']
##################################################params need to be modified########################################

########################################################  merge  ####################################################
if __name__ == '__main__':
    # parallel
    mp.set_start_method('spawn', force=True)
    for sta in sta_list:

        waveform_dir = os.path.join(data_dir, sta)
        
        # get the information of the station
        for k in range(sta_info.shape[0]):
            if int(sta) == sta_info[k, 0]:
                sta_lon = sta_info[k, 1]
                sta_lat = sta_info[k, 2]
                sta_el  = sta_info[k, 3]

        for chn in chns:
            print('Merge for %s-%s' % (sta, chn))
            waveform_list = glob.glob(waveform_dir + '/' + '*' + chn + '*')

            st = Stream()
            for waveform in waveform_list:
                try:
                    tr = read(waveform)[0]
                    # avoid the error from sampling rate
                    if tr.stats.sampling_rate == 100.0:
                        # read the waveform and 
                        st += read(waveform)
                except:
                    print('Bad Data')

            # information of th channels
            if chn == 'EHN':
                cmpaz = 0
                cmpinc = 90
            elif chn == 'EHE':
                cmpaz = 90
                cmpinc = 90
            elif chn == 'EHZ':
                cmpaz = 0
                cmpinc = 0            

            # modify the heads of the traces 
            # in order to merge to one entire channel
            for tr in st:
                tr.stats.network = net
                tr.stats.station = sta
                tr.stats.channel = chn
                tr.stats.location = location

                # add the information of the station to trace
                tr.stats.sac['stlo'] = sta_lon
                tr.stats.sac['stla'] = sta_lat
                tr.stats.sac['stel'] = sta_el
                tr.stats.sac['cmpaz'] = cmpaz
                tr.stats.sac['cmpinc'] = cmpinc

            # Merge the stream sorted by starttime
            # Fill the gaps with 0.            
            st.sort(['starttime'])
            st.merge(method=1, fill_value=0)

            ########################################################  cut  ####################################################
            # cut and save for every channel
            print('Cut for %s-%s' % (sta, chn))
            tr = st[0]
            print(tr.stats.starttime, tr.stats.endtime)
            for i in range(num_days):
                try:
                    # starttime and endtime for cut
                    t0 = start_time + i * 86400
                    t1 = t0 + 86400

                    tr_temp = tr.copy()
                    tr_temp = cut(tr_temp, t0, t1)

                    out_dir = os.path.join(out_data_dir, sta)
                    if not os.path.exists(out_dir): os.makedirs(out_dir)
                    # Refer the format of EQTransformer
                    out_name = net + '.' + sta + '..'  + chn + '__' + dtime2eqt(t0) + '__' + dtime2eqt(t1) + '.SAC'

                    out_path = os.path.join(out_dir, out_name)
                    tr_temp.write(out_path, format='SAC')
                    print('Save to %s.' % (out_path))

                except:
                    print('No data for %s-%s' % (t0, t1))
