'''Pick the arrival times and select the good waveforms.
'''
import os, sys, glob
from obspy import read
sys.path.append('./functions')
from plot import plot_waveform_pick
import matplotlib.pyplot as plt

###################################################params need to be modified####################################
# windows or linux
# platform = 'windows'
platform = 'windows'

# i/o paths
data_dir = ('./events_data_cal_p5+15s_1-10hz')
phase_dir = './output/phase'
if not os.path.exists(phase_dir): os.makedirs(phase_dir)
out_dir = ('./events_data_cal_p5+15s_1-10hz_pick')

# [P-5, P+15]
# time_window = [115, 135]

# pick_type: p or p-s
pick_type = 'p'

event_index = 5
chns = ['EHZ', 'EHN', 'EHE']
###################################################params need to be modified####################################

event_list = os.listdir(data_dir)
event = event_list[event_index]

phase_file_name = 'phase' + '_' + event + '.dat'
phase_file_path = os.path.join(phase_dir, phase_file_name)
f = open(phase_file_path, 'w')

waveform_dir = os.path.join(data_dir, event)
waveform_list = glob.glob(waveform_dir + '/' + '*' + chns[0] + '*')
# print(waveform_list, len(waveform_list))

waveform_pick_dir = os.path.join(out_dir, event)
if not os.path.exists(waveform_pick_dir): os.makedirs(waveform_pick_dir)

# Functions for selecting and picking.
phase=[]
def Pick(event):
    # Left mouse button
    if event.button == 1:
        global phase
        phase.append(event.xdata)
        print("Phase arrivals:", event.xdata)
    # Right mouse button 
    elif event.button == 9: 
        phase=[]
        print('Clear picks, click left button again')
    elif event.button == 3:
        plt.close()
        if len(phase) == 0:
            print('No picks')

for waveform in waveform_list:

    if platform == 'windows':
        # for windows
        sta_id = waveform.split('\\')[-1].split('_')[0]
    else:
        # for linux
        sta_id = waveform.split('/')[-1].split('_')[0]
    print('Select for %s, %s' % (event,sta_id))

    # try:
    waveformpath_z = glob.glob(waveform_dir + '/' + sta_id + '*' + chns[0] + '*')[0]
    waveformpath_n = glob.glob(waveform_dir + '/' + sta_id + '*' + chns[1] + '*')[0]
    waveformpath_e = glob.glob(waveform_dir + '/' + sta_id + '*' + chns[2] + '*')[0]
    # print(waveformpath_Z, waveformpath_N, waveformpath_E)

    tr_z = read(waveformpath_z)[0]
    tr_n = read(waveformpath_n)[0]
    tr_e = read(waveformpath_e)[0]

    # path for picked waveform
    if platform == 'windows':
        # for windows
        waveformpath_z_pick_name = waveformpath_z.split('\\')[-1]
        waveformpath_n_pick_name = waveformpath_n.split('\\')[-1]
        waveformpath_e_pick_name = waveformpath_e.split('\\')[-1]
    else:
        # for linux
        waveformpath_z_pick_name = waveformpath_z.split('/')[-1]
        waveformpath_n_pick_name = waveformpath_n.split('/')[-1]
        waveformpath_e_pick_name = waveformpath_e.split('/')[-1]

    waveform_z_pick_path = os.path.join(waveform_pick_dir, waveformpath_z_pick_name)
    waveform_n_pick_path = os.path.join(waveform_pick_dir, waveformpath_n_pick_name)
    waveform_e_pick_path = os.path.join(waveform_pick_dir, waveformpath_e_pick_name)
    # print(waveform_e_pick_path)

    params_3chns = {'tr_z': tr_z,
                    'tr_n': tr_n,
                    'tr_e': tr_e,
                    'figure_name': sta_id,
                    'pick_type': pick_type
                    }
    fig = plot_waveform_pick(**params_3chns)
    fig.canvas.mpl_connect('button_press_event', Pick)
    plt.show()
    
    # Pick P only
    if len(phase) == 1:
        # p_t = tr_z.stats.starttime + phase[0]            # absolute time of p
        # eq_o = tr_z.stats.starttime - tr_z.stats.sac['b']
        # p_pick = p_t - eq_o
        p_pick = phase[0] + tr_z.stats.sac['b']
        # print(tr_z.stats.sac['user9'], p_pick)
        # add the picked p to 'user7'(the time relative to eq_o)
        tr_z.stats.sac['user7'] = p_pick
        tr_n.stats.sac['user7'] = p_pick
        tr_e.stats.sac['user7'] = p_pick

        f.write('%s %.3f\n' % (sta_id, phase[0]))

        tr_z.write(waveform_z_pick_path, format='SAC')
        tr_n.write(waveform_n_pick_path, format='SAC')
        tr_e.write(waveform_e_pick_path, format='SAC')

    # Pick P and S
    if len(phase) == 2:
        p_pick = phase[0] + tr_z.stats.sac['b']
        s_pick = phase[0] + tr_z.stats.sac['b']
        # add the picked p to user7 and s to user6
        tr_z.stats.sac['user7'] = p_pick
        tr_n.stats.sac['user7'] = p_pick
        tr_e.stats.sac['user7'] = p_pick
        tr_z.stats.sac['user6'] = s_pick
        tr_n.stats.sac['user6'] = s_pick
        tr_e.stats.sac['user6'] = s_pick

        f.write('%s %.3f %.3f\n' % (sta_id, phase[0], phase[1]))

        tr_z.write(waveform_z_pick_path, format='SAC')
        tr_n.write(waveform_n_pick_path, format='SAC')
        tr_e.write(waveform_e_pick_path, format='SAC')
    # Clear the phase and process the next pick.
    phase=[]

    # except:
        # print('There are not enough waveforms.')

waveforms_seleceted = os.listdir(waveform_pick_dir)
print('Selected %f waveforms and picked %f arrivals' % (len(waveforms_seleceted) / 3, len(waveforms_seleceted) / 3))
f.close()
