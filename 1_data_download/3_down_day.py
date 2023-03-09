""" An example for downloading data for continuous waveforms by massdownloader
"""

# TA.R20A and IC.MDJ
# time 20080201-20090201

import os
from obspy import UTCDateTime
from obspy.clients.fdsn.mass_downloader import RectangularDomain, Restrictions, MassDownloader

# i/o paths
data_dir = './waveforms'
sta_dir = './station_xml'

# down params
providers = ["IRIS"]
chn_codes = ['BHZ']

# * for TA.R20A, 10 for IC.MDJ
loc_codes = [["*"], ["10"]]
net = ['TA', 'IC']
sta = ['R20A', 'MDJ']

num_workers = 10

start_date, end_date = UTCDateTime('2008-02-01T00:00:00'), UTCDateTime('2009-02-01T00:00:00')
# start_date, end_date = UTCDateTime('2008-02-01T00:00:00'), UTCDateTime('2008-02-01T00:10:00')

lat_rng = [38, 45]
lon_rng = [-109, 130]

num_day = int((end_date - start_date) / 86400) + 1
print('data range:')
print('latitude range: %s'%(lat_rng))
print('longitude range: %s'%(lon_rng))
print('time range: %s'%[start_date, end_date])

domain = RectangularDomain(minlatitude=lat_rng[0], maxlatitude=lat_rng[1],
                           minlongitude=lon_rng[0], maxlongitude=lon_rng[1])

for day_idx in range(num_day):
    
    t0 = start_date + 86400 * day_idx
    t1 = start_date + 86400 * (day_idx+1)
    print('downloading %s'%t0)

    for i in range(len(net)):
        # 1. set domain & restrict
        restrict = Restrictions(
            starttime = t0,
            endtime = t1,
            network = net[i], 
            station = sta[i], 
            channel_priorities = chn_codes,
            location_priorities = loc_codes[i])

        # 2. set storage
        out_dir = os.path.join(data_dir, ''.join(str(t0.date).split('-')))
        if not os.path.exists(out_dir): os.makedirs(out_dir)

        # 3. start download
        mdl = MassDownloader(providers = providers)
        mdl.download(domain, restrict, 
        threads_per_client = num_workers,
        mseed_storage = out_dir,
        stationxml_storage = sta_dir)
