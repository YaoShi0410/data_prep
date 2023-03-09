"""
Download waveforms for event by catalogs.
"""
import os
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.clients.fdsn.mass_downloader import CircularDomain, RectangularDomain, \
    Restrictions, MassDownloader
from obspy import read_events

################################# two functions for formating the time ################################
# two functions for format the time

# get the days of a year from utcdatetime
def utc2julia(date):
    
    year = date.year
    month = date.month
    day = date.day
    
    months = [0,31,59,90,120,151,181,212,243,273,304,334]
    sum = 0

    if 0 < month <= 12:
        sum = months[month-1]
        sum +=day
    else:
        print("month error")
        
    leap = 0
    
    # leap year and month 
    if(year%400==0) or ((year%4)==0) and (year%100!=0):
        leap = 1
    else:
        pass
        
    if(leap==1) and (month>2):
        sum += 1
    else:
        pass
        
    sum = str(sum)
    if len(sum) == 1:
        sum = '00' + sum
    elif len(sum) == 2:
        sum = '0' + sum
    else:
        pass

    return sum

# format the time
def utc2str(time):
    year = str(time.year)
    
    month = str(time.month)
    if len(month) < 2:
        month = '0' + month

    day = str(time.day)
    if len(day) < 2:
        day = '0' + day
    
    date = year + month + day
    
    julia_day = utc2julia(time)
    
    hour = str(time.hour)
    if len(hour) < 2:
        hour = '0' + hour
        
    minute = str(time.minute)
    if len(minute) < 2:
        minute = '0' + minute
    
    second = str(time.second)
    if len(second) < 2:
        second = '0' + second
    
    microsecond = str(time.microsecond)[0:3]
    if len(microsecond) < 2:
        microsecond = microsecond + '00'
    
    time = hour + '.' + minute + '.' + \
           second + '.' + microsecond
    st_time = date + '.' + julia_day + '.' + time
    
    return st_time

############################### the paths for the waveforms and its related informations ########################
data_dir = '/home/yaoshi/Documents/US_jif3D/seismic_data/'
data_f = open(data_dir + '/data_fail.txt', 'w')

############################### get the station from the file(download from iris/gmap) ###########################
net = 'TA'
stas = []
sta_info = open(data_dir + 'seis_sta.txt')
lines = sta_info.read().splitlines()
for line in lines:
    sta = line.split('|')[1]
    stas.append(sta)

############################### params for download ####################################
# load the catalog(in the format of catalog)
client = Client("IRIS")
cat = read_events(data_dir + 'catalog.xml')
for ev in cat[631:]:
#     ev = cat[1]
    info_event = ev.origins
    orign_time = info_event[0].time
    lat = info_event[0].latitude
    lon = info_event[0].longitude 
    info_mag = ev.magnitudes
    mag = info_mag[0].mag 

    # time before and after the event
    time_range = [-1800, 1800]
    t0 = orign_time + time_range[0]
    t1 = orign_time + time_range[1]

    # domian range
    lat_range = [38, 50] 
    lon_range = [-118, -106]

    # set the dir name
    # 1 dir for 1 event
    str_time = utc2str(orign_time)
    event_name = str_time + '_' + str(mag)

    waveform_dir = data_dir + 'data/' + event_name
    if not os.path.exists(waveform_dir): os.makedirs(waveform_dir)
    print('Event: %s' % (event_name))

############################### Download by MassDownloader #######################
    # station_dir = data_dir  + 'stations'
    # domain = CircularDomain(latitude = lat, longitude = lon,
    #                         minradius = 0, maxradius = 3)
    # domain = RectangularDomain(minlatitude=lat_range[0], maxlatitude=lat_range[1],
    #                            minlongitude=lon_range[0], maxlongitude=lon_range[1])
    
    # for sta in stas:
    #     restrictions = Restrictions(
    #         starttime = t0,
    #         endtime = t1,
    #         network = net,
    #         station = stas,
    #         channel_priorities = ["BH*"])

    #     mdl = MassDownloader(providers = ['IRIS'])
    #     mdl.download(domain, restrictions, threads_per_client = 10, 
    #                 mseed_storage = waveform_dir,
    #                 stationxml_storage = station_dir)

############################### Download by get_waveforms #########################
    for sta in stas:
        # try:
        st = client.get_waveforms(net, sta, "*", "BH*", t0, t1, attach_response = True)
        for i in range(len(st)):
                msd_name = '.'.join([event_name, sta, st[i].stats.channel, 'SAC'])
                out_path = os.path.join(waveform_dir, msd_name)
                st[i].write(out_path, format="SAC")
        print("Get the data for %s" % (sta))
        # except:
        print('%s has no data' % sta)
        data_f.write('{},{},{}\n'.format(event_name, net, sta))

data_f.close()
print('You have downloaded all eligible data')

