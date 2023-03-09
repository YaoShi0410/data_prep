import os
from obspy import read
import torch.multiprocessing as mp

###################################################params need to be modified####################################
# i/o paths
data_dir = ('./events_data_cal_p5+s25s')
out_dir = ('./events_data_cal_p5+s25s_1-10hz')
if not os.path.exists(out_dir): os.makedirs(out_dir)

# frequency range for bandpass
filter_range = filter_range = [1, 10]
###################################################params need to be modified####################################

# Event list
event_list = sorted(os.listdir(data_dir))
if __name__ == '__main__':
    # parallel
    mp.set_start_method('spawn', force=True)

    for event in event_list:

        # directories for every event
        waveform_dir = os.path.join(data_dir, event)
        waveform_list = sorted(os.listdir(waveform_dir))

        for waveform in waveform_list:
            # path for waveform
            waveform_path = os.path.join(waveform_dir, waveform)
            
            try:
                st = read(waveform_path)
                tr = st[0]

                tr.filter('bandpass', freqmin = filter_range[0], freqmax = filter_range[1], zerophase = True) # filter

                # define the output dir and name
                data_filter_dir = os.path.join(out_dir, event)
                if not os.path.exists(data_filter_dir): os.makedirs(data_filter_dir)
                data_filter_path = os.path.join(data_filter_dir, waveform)

                print(data_filter_path)
                tr.write(data_filter_path, format='SAC')
        
            except:
                print('Bad Data!')
