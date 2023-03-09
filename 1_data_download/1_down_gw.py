"""Download data with obspy get_waveforms 
"""
import os, sys
sys.path.append('/home/yaoshi/seismic_data')
import obspy
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from reader import dtime2str

# the information of net and station 
sta_info = './input/net_sta.csv'
# the location of downloaded data
data_dir = './data'
# failure records
data_f = open('./output/data_fail.dat', 'w')

# download parameters
client = Client("IRIS")
start_time = UTCDateTime('2007-12-31T00:00:00.00')
end_time = UTCDateTime('2008-01-01T00:00:00')
num_days = int((end_time - start_time) / 86400) + 1

# save the information of net and station to list
f = open(sta_info)
# remove '/n'
lines = f.read().splitlines()
f.close()
net_sta_list = [line.split(',')[0].split('.') for line in lines]

#download data in days
for day_i in range(num_days):
    for (net, sta) in net_sta_list:
        t0 = start_time + 86400 * day_i
        t1 = t0 + 86400
        print(net, sta, t0, t1)
    
        # download waveform data, save the data in same dir from same station
        try:
            # all channels in a file
        
            #st = client.get_waveforms(net, sta, "*", "BN*", t0, t1)
            #print(net, sta, st[0].stats["starttime"])
            #dtime = dtime2str(t0)
            #msd_name = '.'.join([net,sta,dtime,'mseed'])
            #msd_dir = os.path.join(data_dir,net,sta)
            #out_path = os.path.join(msd_dir, msd_name)
            #if not os.path.exists(msd_dir): os.makedirs(msd_dir)
            #st.write(out_path, format="MSEED")
                
        
            # one channel for a file
            st = client.get_waveforms(net, sta, "*", "BH*", t0, t1, attach_response = True)
            print(net, sta, st[0].stats["starttime"])
            dtime = dtime2str(t0)
            msd_dir = os.path.join(data_dir, net, sta)
            if not os.path.exists(msd_dir): os.makedirs(msd_dir)        
            for i in range(len(st)):
                msd_name = '.'.join([net, sta, dtime, st[i].stats.channel, 'mseed'])
                out_path = os.path.join(msd_dir, msd_name)
                st[i].write(out_path, format="MSEED")
        except:
            print('no data')
            data_f.write('{},{},{}\n'.format(net,sta,t0))
data_f.close()

