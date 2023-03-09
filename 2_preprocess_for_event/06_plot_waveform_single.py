"""Select good waveforms. 
"""
import os, sys, shutil
sys.path.append('./functions')
from plot import plot_waveform_single

#############################################params need to be modified#######################################
# i/o paths
data_dir = ('./events_data_cal_p2+s2mins_0.1-1hz')
# fig_dir = 

fig_size = (10, 4)

# time for p and s
time_range = [115, 135]
#############################################params need to be modified#######################################

# event list
event_list = sorted(os.listdir(data_dir))
print('There are total %d events' % (len(event_list)))

event = event_list[0]
waveform_dir = os.path.join(data_dir, event)
waveform_list = sorted(os.listdir(waveform_dir))

print('Select For %s' % (event))

for waveform in waveform_list:
    
    # path for raw waveform
    waveform_path = os.path.join(waveform_dir, waveform)
    
    # plot the waveform
    # plot_waveform(waveform_path=waveform_path, event_name=event, time_before_p=p_before, time_after_s=s_after, type='cal')
    plot_params = {'waveform_path': waveform_path, 
                   'event': event,
                   'fig_size': fig_size,
                   'time_range': time_range
                  }
    plot_waveform_single(**plot_params)

