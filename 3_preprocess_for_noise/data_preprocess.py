""""
Preprocess for noise data.
"""
import os, sys
from obspy import read, read_inventory
sys.path.append('/home/yaoshi/seismic_data')
from normalization import normalize, whiten
from reader import dtime2str

# file params
os.chdir("/home/yaoshi/seismic_data/data_test/20080101")
file_list = os.listdir()
out_dir = ("/home/yaoshi/seismic_data/data_test/20080101_processed")

# params for removing instrument and filter
pre_filt = (0.001, 0.005, 10, 20)
inv = read_inventory('../eg_stations/1A.NE24.xml')
filter_range = [0.05, 0.2]

for i in range(len(file_list)):
    st = read(file_list[i])
    tr = st[0]
    # remove response for a staion using a station XMl file
    # XML file needs to be downloaded
    tr.remove_response(inventory = inv,  output = 'DISP', pre_filt = pre_filt)
    # Note that the  automatically includes a lowpass filtering with corner frequency: 
    # 0.4 * sampling_rate / factor.
    tr.decimate(factor = 4, strict_length = False)

    tr.detrend("demean") # rmean
    tr.detrend("linear") # rtrend
    tr.taper(max_percentage = 0.05, type = 'cosine') # taper
    tr.filter('bandpass', freqmin = filter_range[0], freqmax = filter_range[1], zerophase = True) # filter

    # Temporal and Spectural noramalization
    # Only for nosie correlation
    tr = normalize(tr, norm_win = 10, norm_method = "ramn")
    tr = whiten(tr, filter_range[0], filter_range[1])

    file_name = '.'.join([tr.stats.network, tr.stats.station, dtime2str(tr.stats.starttime), \
                tr.stats.channel, 'sac'])
    out_path = os.path.join(out_dir, file_name)
    tr.write(out_path, format = 'SAC')


