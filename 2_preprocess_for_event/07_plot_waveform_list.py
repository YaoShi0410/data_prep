"""Plot the seismograms by the order of the distance.
"""
import os, glob, sys
sys.path.append('./functions')
import torch.multiprocessing as mp
from plot import plot_waveform_list

############################################params need to be modified##############################################
# windows or linux
# platform = 'windows'
platform = 'windows'

# i/o paths
data_dir = ('./events_data_cal_p5+s15s')
out_dir = ('./figures/events_data_cal_p5+s15s')

# data_dir = ('./events_data_cal_p5+s15s_0.1-5hz_pick')
# out_dir = ('./figures/events_data_cal_p5+s15s_0.1-5hz_pick')

if not os.path.exists(out_dir): os.makedirs(out_dir)

# plot_type: cal, p_pick, p_pick&cal, p-s_pick, p-s_pick&cal, None
plot_type = 'cal'

# for specific stations
sta_id_list = ['100[0-9]', '101[0-9]', '102[0-9]', '103[0-9]', '104[0-9]', '105[0-9]', '106[0-9]', '107[0-9]', '108[0-9]', '109[0-9]',
               '110[0-9]', '111[0-9]', '112[0-9]', '113[0-9]', '114[0-9]', '115[0-9]', '116[0-9]', '117[0-9]', '118[0-9]', '119[0-9]',
               '120[0-9]', '121[0-9]', '122[0-9]', '123[0-9]', '124[0-9]', '125[0-9]', '126[0-9]', '127[0-9]', '128[0-9]', '129[0-9]',
               '130[0-9]', '131[0-9]', '132[0-9]', '133[0-9]', '134[0-9]', '135[0-9]', '136[0-9]', '137[0-9]', '138[0-9]', '139[0-9]',
               '140[0-9]', '141[0-9]', '142[0-9]', '143[0-9]', '144[0-9]', '145[0-9]', '146[0-9]', '147[0-9]', '14[8-9][0-9]'
              ]

# sta_id_list = ['*']


# time_window = str(time_range[0]) + '-' + str(time_range[1])
time_range = None
# time_range = [115, 135]

# channels
chns = ['EHZ', 'EHN', 'EHE']

# figure size
figure_size = (10, 12)

############################################params need to be modified##############################################
event_list = sorted(os.listdir(data_dir))

print('There are total %d events.' % (len(event_list)))

if __name__ == '__main__':
    # parallel
    mp.set_start_method('spawn', force=True)

    for event in event_list:

        waveform_dir = os.path.join(data_dir, event)

        for chn in chns:

            # ############################################ select by sta_id ######################################
            for i in range(len(sta_id_list)):

                sta_id = sta_id_list[i]
                waveform_list = sorted(glob.glob(waveform_dir + '/' + sta_id + '*' + chn + '*'))

                if len(waveform_list) > 0:
                    if platform == 'windows':
                        # for windows
                        sta_list_name = waveform_list[0].split('\\')[-1].split('_')[0] + '-' + waveform_list[-1].split('\\')[-1].split('_')[0]
                    else:
                        # for linux
                        sta_list_name = waveform_list[0].split('/')[-1].split('_')[0] + '-' + waveform_list[-1].split('/')[-1].split('_')[0]
                    print('Plot for %s' % (sta_list_name))            

                    # name for the figure
                    if chn != '*':
                        figure_name = event + '_' + sta_list_name + '_' + chn + '.png'
                    else:
                        figure_name = event + sta_list_name + '.png'
                    
                    # path for the figure
                    if chn == '*':
                        figure_dir = os.path.join(out_dir, event)
                        if not os.path.exists(figure_dir): os.makedirs(figure_dir)
                        figure_path = os.path.join(figure_dir, figure_name)
                    else:
                        figure_dir = os.path.join(out_dir, event, chn)
                        if not os.path.exists(figure_dir): os.makedirs(figure_dir)
                        figure_path = os.path.join(figure_dir, figure_name)
                    
                    # plot the results
                    print('Plot for %d stations and save as %s.' % (len(waveform_list), figure_path))
                    plot_params = {'waveform_list': waveform_list,
                                    'figure_path': figure_path,
                                    'title': figure_name, 
                                    'fig_size': figure_size,
                                    'time_range': time_range,
                                    'type': plot_type
                                    }
                    plot_waveform_list(**plot_params)

