'''Prepare for ESPRH. (Make station_list.json and sta_info_real_format.dat)
'''
import os
import json
import numpy as np

########################################################202109#####################################################################
################################AEJ_Stations##################################
# i/o paths
# stations from AEJ profile
sta_info_file = ('./input/AEJ_sta_info.txt')
sta_info = open(sta_info_file, 'r')
lines = sta_info.read().splitlines()
num_AEJ_stas = len(lines)
sta_info.close()
print('There are total %d stations in AEJ profiles' % (num_AEJ_stas))

# stations from AEJ profile in 202109
data_dir = './202109/AEJ'
sta_list= sorted(os.listdir(data_dir))
print('There are total %d stations in 202109 from AEJ profiles.' % (len(sta_list)))

# outdir
out_dir = ('./output')
if not os.path.exists(out_dir): os.makedirs(out_dir)

# known informations
chns = ["EHZ", "EHE", "EHN"]
AEJ_station_list = {}

for line in lines:
    net  = line.split(' ')[0]
    sta  = str(line.split(' ')[1])
    stla = line.split(' ')[2]
    stlo = line.split(' ')[3]
    stel = line.split(' ')[4]

    if sta in sta_list:
        coords = [stla, stlo, stel]
        AEJ_station_list[sta] = {"network": net,
                             "channels": chns,
                             "coords": coords
                            } 

with open(out_dir + '/202109_AEJ_station_list.json', 'w') as fp:
    json.dump(AEJ_station_list, fp)

################################CHN_Stations##################################
# i/o paths
# stations from CHN
sta_info_file = ('./input/CHN_sta_info.txt')
sta_info = open(sta_info_file, 'r')
lines = sta_info.read().splitlines()
num_CHN_stas = len(lines)
sta_info.close()
print('There are total %d stations in CHN stations' % (num_CHN_stas))

# stations from CHN in 202109
data_dir = './202109/CHN'
sta_list= sorted(os.listdir(data_dir))
print('There are total %d stations in 202109 from CHN stations.' % (len(sta_list)))

# outdir
out_dir = ('./output')
if not os.path.exists(out_dir): os.makedirs(out_dir)

# known informations
chns = ["LHZ", "LHE", "LHN"]
CHN_station_list = {}

for line in lines:
    net  = line.split(' ')[0]
    sta  = str(line.split(' ')[1])
    stla = line.split(' ')[2]
    stlo = line.split(' ')[3]
    stel = line.split(' ')[4]

    if sta in sta_list:
        coords = [stla, stlo, stel]
        CHN_station_list[sta] = {"network": net,
                             "channels": chns,
                             "coords": coords
                            } 

with open(out_dir + '/202109_CHN_station_list.json', 'w') as fp:
    json.dump(CHN_station_list, fp)

################################ALL_Stations##################################
station_list = {}
station_list.update(AEJ_station_list)
station_list.update(CHN_station_list)
print('There are total %d stations in 202109.' % (len(station_list)))

with open(out_dir + '/202109_station_list.json', 'w') as fp:
    json.dump(station_list, fp)

########################################################202110#####################################################################
################################AEJ_Stations##################################
# i/o paths
# stations from AEJ profile
sta_info_file = ('./input/AEJ_sta_info.txt')
sta_info = open(sta_info_file, 'r')
lines = sta_info.read().splitlines()
num_AEJ_stas = len(lines)
sta_info.close()
print('There are total %d stations in AEJ profiles' % (num_AEJ_stas))

# stations from AEJ profile in 202110
data_dir = './202110/AEJ'
sta_list= sorted(os.listdir(data_dir))
print('There are total %d stations in 202110 from AEJ profiles.' % (len(sta_list)))

# outdir
out_dir = ('./output')
if not os.path.exists(out_dir): os.makedirs(out_dir)

# known informations
chns = ["EHZ", "EHE", "EHN"]
AEJ_station_list = {}

for line in lines:
    net  = line.split(' ')[0]
    sta  = str(line.split(' ')[1])
    stla = line.split(' ')[2]
    stlo = line.split(' ')[3]
    stel = line.split(' ')[4]

    if sta in sta_list:
        coords = [stla, stlo, stel]
        AEJ_station_list[sta] = {"network": net,
                             "channels": chns,
                             "coords": coords
                            } 

with open(out_dir + '/202110_AEJ_station_list.json', 'w') as fp:
    json.dump(AEJ_station_list, fp)

################################CHN_Stations##################################
# i/o paths
# stations from CHN
sta_info_file = ('./input/CHN_sta_info.txt')
sta_info = open(sta_info_file, 'r')
lines = sta_info.read().splitlines()
num_CHN_stas = len(lines)
sta_info.close()
print('There are total %d stations in CHN stations' % (num_CHN_stas))

# stations from CHN in 202110
data_dir = './202110/CHN'
sta_list= sorted(os.listdir(data_dir))
print('There are total %d stations in 202110 from CHN stations.' % (len(sta_list)))

# outdir
out_dir = ('./output')
if not os.path.exists(out_dir): os.makedirs(out_dir)

# known informations
chns = ["LHZ", "LHE", "LHN"]
CHN_station_list = {}

for line in lines:
    net  = line.split(' ')[0]
    sta  = str(line.split(' ')[1])
    stla = line.split(' ')[2]
    stlo = line.split(' ')[3]
    stel = line.split(' ')[4]

    if sta in sta_list:
        coords = [stla, stlo, stel]
        CHN_station_list[sta] = {"network": net,
                             "channels": chns,
                             "coords": coords
                            } 

with open(out_dir + '/202110_CHN_station_list.json', 'w') as fp:
    json.dump(CHN_station_list, fp)

################################ALL_Stations##################################
station_list = {}
station_list.update(AEJ_station_list)
station_list.update(CHN_station_list)
print('There are total %d stations in 202110.' % (len(station_list)))

with open(out_dir + '/202110_station_list.json', 'w') as fp:
    json.dump(station_list, fp)


########################################################202111#####################################################################
################################AEJ_Stations##################################
# i/o paths
# stations from AEJ profile
sta_info_file = ('./input/AEJ_sta_info.txt')
sta_info = open(sta_info_file, 'r')
lines = sta_info.read().splitlines()
num_AEJ_stas = len(lines)
sta_info.close()
print('There are total %d stations in AEJ profiles' % (num_AEJ_stas))

# stations from AEJ profile in 202111
data_dir = './202111/AEJ'
sta_list= sorted(os.listdir(data_dir))
print('There are total %d stations in 202111 from AEJ profiles.' % (len(sta_list)))

# outdir
out_dir = ('./output')
if not os.path.exists(out_dir): os.makedirs(out_dir)

# known informations
chns = ["EHZ", "EHE", "EHN"]
AEJ_station_list = {}

for line in lines:
    net  = line.split(' ')[0]
    sta  = str(line.split(' ')[1])
    stla = line.split(' ')[2]
    stlo = line.split(' ')[3]
    stel = line.split(' ')[4]

    if sta in sta_list:
        coords = [stla, stlo, stel]
        AEJ_station_list[sta] = {"network": net,
                             "channels": chns,
                             "coords": coords
                            } 

with open(out_dir + '/202111_AEJ_station_list.json', 'w') as fp:
    json.dump(AEJ_station_list, fp)

################################CHN_Stations##################################
# i/o paths
# stations from CHN
sta_info_file = ('./input/CHN_sta_info.txt')
sta_info = open(sta_info_file, 'r')
lines = sta_info.read().splitlines()
num_CHN_stas = len(lines)
sta_info.close()
print('There are total %d stations in CHN stations' % (num_CHN_stas))

# stations from CHN in 202111
data_dir = './202111/CHN'
sta_list= sorted(os.listdir(data_dir))
print('There are total %d stations in 202111 from CHN stations.' % (len(sta_list)))

# outdir
out_dir = ('./output')
if not os.path.exists(out_dir): os.makedirs(out_dir)

# known informations
chns = ["LHZ", "LHE", "LHN"]
CHN_station_list = {}

for line in lines:
    net  = line.split(' ')[0]
    sta  = str(line.split(' ')[1])
    stla = line.split(' ')[2]
    stlo = line.split(' ')[3]
    stel = line.split(' ')[4]

    if sta in sta_list:
        coords = [stla, stlo, stel]
        CHN_station_list[sta] = {"network": net,
                             "channels": chns,
                             "coords": coords
                            } 

with open(out_dir + '/202111_CHN_station_list.json', 'w') as fp:
    json.dump(CHN_station_list, fp)

################################ALL_Stations##################################
station_list = {}
station_list.update(AEJ_station_list)
station_list.update(CHN_station_list)
print('There are total %d stations in 202111.' % (len(station_list)))

with open(out_dir + '/202111_station_list.json', 'w') as fp:
    json.dump(station_list, fp)

