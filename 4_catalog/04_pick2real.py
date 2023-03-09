''' Convert the output of EQT to the input of REAL.
'''
import os, shutil
from obspy import UTCDateTime


##################################################convert EQT to REAL##################################################
# i/o paths
# data_dir = '/home/yaoshi/Documents/ESPRH/example/detection_results'
data_dir = '/mnt/f/ESPRH_202109/202109/Original/detection_results'
file_name = 'X_prediction_results.csv'
out_dir = './picks_real_Original'

# startting date and number of days
year0 = '2021'
month0 = '09'
day0 = '17'
nday = 14
date0 = year0 + month0 + day0

for i in range(nday):

    # creat directory for every day
    ref_date = str(int(date0) + i)
    pick_out_dir = os.path.join(out_dir, ref_date)
    if not os.path.exists(pick_out_dir): os.makedirs(pick_out_dir)
    print('ref_date:{}'.format(ref_date))

    # info for stations
    sta_list = sorted(os.listdir(data_dir))
    for sta in sta_list:

        # path for output of EQT
        pick_path = os.path.join(data_dir, sta, file_name)
        print(pick_path)

        f = open(pick_path, 'r')
        lines = f.read().splitlines()[1:]
        f.close()
        
        if len(lines) > 0:
            # create file for every station in this day
            # network and station
            net = lines[0].split(',')[1]
            sta = lines[0].split(',')[2].strip()
            out_p_name = '.'.join([net, sta, 'P', 'txt'])
            out_s_name = '.'.join([net, sta, 'S', 'txt'])
            out_p_path = os.path.join(pick_out_dir, out_p_name)
            out_s_path = os.path.join(pick_out_dir, out_s_name)

            f_p = open(out_p_path, 'w')
            f_s = open(out_s_path, 'w')

            print(out_p_path, out_s_path)

            for line in lines:
                # extract info from output of EQT
                # path for input of real
                try:
                    # arrival time and probability of P wave
                    p_arrival_time = UTCDateTime(line.split(',')[11])
                    p_time = p_arrival_time - UTCDateTime(ref_date)
                    p_probability = float(line.split(',')[12])
                    p_amp = 0.0
                    # date
                    p_year = '%4.4d' % p_arrival_time.year
                    p_mon = '%2.2d' % p_arrival_time.month
                    p_day = '%2.2d' % p_arrival_time.day
                    p_date = str(p_year) + str(p_mon) + str(p_day)
                    if p_date == ref_date:
                        print(p_time, p_probability, p_amp)
                        f_p.write('%f %f %f\n' % (p_time, p_probability, p_amp))
                except:
                    print('No P_arrival')
                
                try:
                    # arrival time and probability of S wave
                    s_arrival_time = UTCDateTime(line.split(',')[15])
                    s_time = s_arrival_time - UTCDateTime(ref_date)
                    s_probability = float(line.split(',')[16])
                    s_amp = 0.0
                    # date
                    s_year = '%4.4d' % s_arrival_time.year
                    s_mon = '%2.2d' % s_arrival_time.month
                    s_day = '%2.2d' % s_arrival_time.day
                    s_date = str(s_year) + str(s_mon) + str(s_day)
                    if s_date == ref_date:
                        print(s_time, s_probability, s_amp)
                        f_s.write('%f %f %f\n' % (s_time, s_probability, s_amp))                
                except:
                    print('No S_arrival')            
            f_p.close()
            f_s.close()

##################################################remove empty files and dirs##################################################
date_list = sorted(os.listdir(out_dir))

# remove empty files
for date in date_list:

    date_dir = os.path.join(out_dir, date)
    file_list = sorted(os.listdir(date_dir))

    for file in file_list:

        file_path = os.path.join(date_dir, file)
        
        f = open(file_path, 'r')
        lines = f.readlines()
        f.close()

        if len(lines) == 0:
            os.remove(file_path)
            print('remove %s' % (file_path))

# remove empty dirs
for date in date_list:

    date_dir = os.path.join(out_dir, date)
    file_list = sorted(os.listdir(date_dir))

    if len(file_list) == 0:

        shutil.rmtree(date_dir)
        print('remove %s' % (date_dir))
