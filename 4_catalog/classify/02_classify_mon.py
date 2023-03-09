'''Classify the data_day by month.(To satisfy the need of ESPRH) 
'''
import os
import shutil

# params need be modified
data_dir = './data'
out_dir = 'H:/data_day'

sta_list = os.listdir(data_dir)
print('There are total %d stations.' % (len(sta_list)))

mon_list = ['202109', '202110', '202111']
print('There are total %d months.' % (len(mon_list)))

for mon in mon_list:

    for sta in sta_list:

        waveform_dir = os.path.join(data_dir, sta)
        waveform_list = os.listdir(waveform_dir)

        for waveform in waveform_list:

            waveform_mon = waveform.split('__')[1][:6]
            # print(waveform_mon)

            if waveform_mon == mon:

                waveform_path = os.path.join(waveform_dir, waveform)
                waveform_out_dir = os.path.join(out_dir, mon, sta)
                if not os.path.exists(waveform_out_dir): os.makedirs(waveform_out_dir)

                waveform_out_path = os.path.join(waveform_out_dir, waveform)

                print('%s -> %s' % (waveform_path, waveform_out_path))
                shutil.copy(waveform_path, waveform_out_path)

