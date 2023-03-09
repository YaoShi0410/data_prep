import sys
from obspy import UTCDateTime

# from time_convert import time2utc
f = open('./catalog_utc+8.txt')
cats = f.read().splitlines()
eq_o_list = []
eq_lat_list = []
eq_lon_list = []
eq_mag_list = []
eq_dep_list = []
for cat in cats:
    eq_o = UTCDateTime(cat.split(' ')[0]) - 8 * 3600
    # print(eq_o)
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

with open('./catalog.txt', 'w') as f:
    for i in range(len(eq_o_list)):
        f.write('%s %s %s %s %s\n' % 
        (eq_o_list[i], eq_lat_list[i], eq_lon_list[i], eq_mag_list[i], eq_dep_list[i]))
