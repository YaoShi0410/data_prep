"""
Downdload catalogs for specific earthquakes.
"""
from obspy import UTCDateTime
from obspy.clients.fdsn import Client

client = Client("IRIS")

# the path to the file for catalogs
cat_path = './catalog.txt'

# parameters for events
t1 = UTCDateTime('1970-01-01T00:00:00')
t2 = UTCDateTime('2022-11-21T00:00:00')
# domain range
lat_range = [17, 27] 
lon_range = [121, 127]
mag_range = [0, 10]

params = {
            'starttime' : t1, 
            'endtime' : t2,
            'minlatitude' : lat_range[0],
            'maxlatitude' : lat_range[1],
            'minlongitude' : lon_range[0],
            'maxlongitude' : lon_range[1],
            'minmagnitude' : mag_range[0],
            'maxmagnitude' : mag_range[1]
        }

cat = client.get_events(**params)
print('There are total %d events' % (cat.count())) 

# save to a xml file
# cat.write('./catalog.xml', format='QUAKEML')

# from obspy import read_events
# cat1 = read_events('/home/yaoshi/Documents/US_jif3D/catalog.xml')

# save the infomation of events to a text.
cat_file = open(cat_path, 'w')

for ev in cat:
    info_event = ev.origins
    orign_time = info_event[0].time
    lat = info_event[0].latitude
    lon = info_event[0].longitude
    dep = info_event[0].depth
    
    info_mag = ev.magnitudes
    mag = info_mag[0].mag
    
    cat_file.write('%s|%s|%s|%s|%s\n' % (orign_time, lat, lon, mag, dep))

cat_file.close()
