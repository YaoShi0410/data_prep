'''Delete the bad data. By the time, data_type and channel.
'''
import os, shutil
import torch.multiprocessing as mp

##################################################params need to be modified########################################
# dir for raw data
raw_dir = 'G:/AEJ_raw/foldersac'
sta_list = sorted(os.listdir(raw_dir))

print("Thereare total %d stations" % (len(sta_list)))
# dir for out dat
out_dir = 'G:/AEJ_raw/bad_data'
if not os.path.exists(out_dir): os.makedirs(out_dir)

chns = ['EHZ', 'EHN', 'EHE']
##################################################params need to be modified########################################

if __name__ == '__main__':
    # parallel
    mp.set_start_method('spawn', force=True)
    for sta in sta_list:
        waveform_dir = os.path.join(raw_dir, sta)
        waveform_list = sorted(os.listdir(waveform_dir))

        for waveform in waveform_list:
            waveform_path = os.path.join(waveform_dir, waveform)

            out_name = sta + '_' + waveform
            out_path = os.path.join(out_dir, out_name)
            # print(out_name)
            try:
                year = waveform[:4]
                data_type = waveform.split('.')[-1]
                chn = waveform.split('.')[-2]
                # print(year, data_type, chn)
                if year != '2021' or data_type != 'SAC' or chn not in chns:
                    shutil.move(waveform_path, out_path)
                    print(waveform_path, out_path)
            except:
                shutil.move(waveform_path, out_path)
                print(waveform_path, out_path)

