'''Prepare station.dat for Loc-flow.CHN
'''
import os
import numpy as np

########################################################202109#####################################################################
################################AEJ_Stations##################################
# i/o paths
sta_info_file = ('./input/AEJ_sta_info.txt')
out_file = ('./output/202109_AEJ_station.dat')

sta_list = sorted(os.listdir('./202109/AEJ'))
print('There are total %d AEJ stations in 202109' % len(sta_list))
# print(sta_list)

f = open(sta_info_file, 'r')
lines = f.read().splitlines()
f.close()
print('There are total %d AEJ stations' % len(lines))

with open(out_file, 'w') as f:

    for line in lines:

        net = line.split(' ')[0]
        sta = str(line.split(' ')[1])
        stla = float(line.split(' ')[2])
        stlo = float(line.split(' ')[3])
        stel = float(line.split(' ')[4]) / 1e3
        chn = 'EHZ'

        # print(net, sta, stla, stlo, stel)

        if sta in sta_list:
            f.write('%.4f %.4f %s %s %s %.3f\n' % 
                    (stlo, stla, net, sta, chn, stel))   

################################CHN_Stations##################################
# i/o paths
sta_info_file = ('./input/CHN_sta_info.txt')
out_file = ('./output/202109_CHN_station.dat')

sta_list = sorted(os.listdir('./202109/CHN'))
print('There are total %d CHN stations in 202109' % len(sta_list))
# print(sta_list)

f = open(sta_info_file, 'r')
lines = f.read().splitlines()
f.close()
print('There are total %d CHN stations' % len(lines))

with open(out_file, 'w') as f:

    for line in lines:

        net = line.split(' ')[0]
        sta = str(line.split(' ')[1])
        stla = float(line.split(' ')[2])
        stlo = float(line.split(' ')[3])
        stel = float(line.split(' ')[4]) / 1e3
        chn = 'LHZ'

        # print(net, sta, stla, stlo, stel)

        if sta in sta_list:
            f.write('%.4f %.4f %s %s %s %.3f\n' % 
                    (stlo, stla, net, sta, chn, stel))  

################################ALL_Stations##################################
os.system("awk '{print $1,$2,$3,$4,$5,$6}' ./output/202109_AEJ_station.dat > ./output/202109_station.dat")
os.system("awk '{print $1,$2,$3,$4,$5,$6}' ./output/202109_CHN_station.dat >> ./output/202109_station.dat")

########################################################202110#####################################################################
################################AEJ_Stations##################################
# i/o paths
sta_info_file = ('./input/AEJ_sta_info.txt')
out_file = ('./output/202110_AEJ_station.dat')

sta_list = sorted(os.listdir('./202110/AEJ'))
print('There are total %d AEJ stations in 202110' % len(sta_list))
# print(sta_list)

f = open(sta_info_file, 'r')
lines = f.read().splitlines()
f.close()
print('There are total %d AEJ stations' % len(lines))

with open(out_file, 'w') as f:

    for line in lines:

        net = line.split(' ')[0]
        sta = str(line.split(' ')[1])
        stla = float(line.split(' ')[2])
        stlo = float(line.split(' ')[3])
        stel = float(line.split(' ')[4]) / 1e3
        chn = 'EHZ'

        # print(net, sta, stla, stlo, stel)

        if sta in sta_list:
            f.write('%.4f %.4f %s %s %s %.3f\n' % 
                    (stlo, stla, net, sta, chn, stel))   

################################CHN_Stations##################################
# i/o paths
sta_info_file = ('./input/CHN_sta_info.txt')
out_file = ('./output/202110_CHN_station.dat')

sta_list = sorted(os.listdir('./202110/CHN'))
print('There are total %d CHN stations in 202110' % len(sta_list))
# print(sta_list)

f = open(sta_info_file, 'r')
lines = f.read().splitlines()
f.close()
print('There are total %d CHN stations' % len(lines))

with open(out_file, 'w') as f:

    for line in lines:

        net = line.split(' ')[0]
        sta = str(line.split(' ')[1])
        stla = float(line.split(' ')[2])
        stlo = float(line.split(' ')[3])
        stel = float(line.split(' ')[4]) / 1e3
        chn = 'LHZ'

        # print(net, sta, stla, stlo, stel)

        if sta in sta_list:
            f.write('%.4f %.4f %s %s %s %.3f\n' % 
                    (stlo, stla, net, sta, chn, stel))  

################################ALL_Stations##################################
os.system("awk '{print $1,$2,$3,$4,$5,$6}' ./output/202110_AEJ_station.dat > ./output/202110_station.dat")
os.system("awk '{print $1,$2,$3,$4,$5,$6}' ./output/202110_CHN_station.dat >> ./output/202110_station.dat")

########################################################202111#####################################################################
################################AEJ_Stations##################################
# i/o paths
sta_info_file = ('./input/AEJ_sta_info.txt')
out_file = ('./output/202111_AEJ_station.dat')

sta_list = sorted(os.listdir('./202111/AEJ'))
print('There are total %d AEJ stations in 202111' % len(sta_list))
# print(sta_list)

f = open(sta_info_file, 'r')
lines = f.read().splitlines()
f.close()
print('There are total %d AEJ stations' % len(lines))

with open(out_file, 'w') as f:

    for line in lines:

        net = line.split(' ')[0]
        sta = str(line.split(' ')[1])
        stla = float(line.split(' ')[2])
        stlo = float(line.split(' ')[3])
        stel = float(line.split(' ')[4]) / 1e3
        chn = 'EHZ'

        # print(net, sta, stla, stlo, stel)

        if sta in sta_list:
            f.write('%.4f %.4f %s %s %s %.3f\n' % 
                    (stlo, stla, net, sta, chn, stel))   

################################CHN_Stations##################################
# i/o paths
sta_info_file = ('./input/CHN_sta_info.txt')
out_file = ('./output/202111_CHN_station.dat')

sta_list = sorted(os.listdir('./202111/CHN'))
print('There are total %d CHN stations in 202111' % len(sta_list))
# print(sta_list)

f = open(sta_info_file, 'r')
lines = f.read().splitlines()
f.close()
print('There are total %d CHN stations' % len(lines))

with open(out_file, 'w') as f:

    for line in lines:

        net = line.split(' ')[0]
        sta = str(line.split(' ')[1])
        stla = float(line.split(' ')[2])
        stlo = float(line.split(' ')[3])
        stel = float(line.split(' ')[4]) / 1e3
        chn = 'LHZ'

        # print(net, sta, stla, stlo, stel)

        if sta in sta_list:
            f.write('%.4f %.4f %s %s %s %.3f\n' % 
                    (stlo, stla, net, sta, chn, stel))  

################################ALL_Stations##################################
os.system("awk '{print $1,$2,$3,$4,$5,$6}' ./output/202111_AEJ_station.dat > ./output/202111_station.dat")
os.system("awk '{print $1,$2,$3,$4,$5,$6}' ./output/202111_CHN_station.dat >> ./output/202111_station.dat")

