'''Make the fname.csv for phasenet.
'''
import os

data_dir = './waveform_sac'

out_file = './fname.csv'

date_list = sorted(os.listdir(data_dir))

fname_list = []

for date in date_list:
    waveform_dir = os.path.join(data_dir, date)
    waveform_list = sorted(os.listdir(waveform_dir))


    for waveform in waveform_list:
        fname = date + '/' + waveform[:-1] + '*'

        if fname not in fname_list:
            fname_list.append(fname)

print('There are total %d 3 channels data.' % len(fname_list))

with open(out_file, 'w') as f:

    f.write('fname\n')
    
    for fname in fname_list:

        f.write('%s\n' % fname)