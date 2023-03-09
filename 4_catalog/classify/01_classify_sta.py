'''Classify the data by station.
'''
import os
import shutil

data_dir = './data'

sta_list = []
date_list = sorted(os.listdir(data_dir))

for date in date_list:

    waveform_dir = os.path.join(data_dir, date)
    waveform_list = sorted(os.listdir(waveform_dir))

    for waveform in waveform_list:

        sta = waveform.split('.')[1]
        waveform_path = os.path.join(waveform_dir, waveform)

        if sta not in sta_list:

            sta_list.append(sta)

        # move the waveform from date_dir to sta_dir
        waveform_out_dir = os.path.join(data_dir, sta)
        if not os.path.exists(waveform_out_dir): os.makedirs(waveform_out_dir)
        waveform_out_path = os.path.join(waveform_out_dir, waveform)

        shutil.move(waveform_path, waveform_out_path)

        print(waveform_path, waveform_out_path)

print('There are total {} stations.'.format(len(sta_list)))

# delete the empty folders
for dir in os.listdir(data_dir):

    waveform_dir = os.path.join(data_dir, dir)
    print(waveform_dir, len(os.listdir(waveform_dir)))

    if len(os.listdir(waveform_dir)) == 0:

        os.rmdir(waveform_dir)
