'''Prepare for locflow.
'''
import os
import shutil

data_dir = './202111'

# out_dir = './waveform_sac'
out_dir = 'H:/Locflow_202111/waveform_sac'

sta_list = os.listdir(data_dir)
print('There are total %d stations' % (len(sta_list)))

for sta in sta_list:

    waveform_dir = os.path.join(data_dir, sta)
    waveform_list = os.listdir(waveform_dir)

    for waveform in waveform_list:

        net = waveform.split('.')[0]
        sta = waveform.split('.')[1]
        chn = waveform.split('.')[3].split('__')[0]
        date = waveform.split('__')[1].split('T')[0]

        waveform_path = os.path.join(waveform_dir, waveform)

        waveform_out_dir = os.path.join(out_dir, date)
        if not os.path.exists(waveform_out_dir): os.makedirs(waveform_out_dir)
        waveform_out_name = '.'.join([net, sta, chn])
        waveform_out_path = os.path.join(waveform_out_dir, waveform_out_name)

        print(waveform_path, waveform_out_path)
        shutil.copy(waveform_path, waveform_out_path)

