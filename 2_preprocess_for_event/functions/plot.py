"""Plot waveform with calculated P and S arrivals.
"""
from obspy import read, Stream
import numpy as np
import matplotlib.pyplot as plt
from time_convert import dtime2int

# Plot the single waveform and label the P and S arivals on it
def plot_waveform_single(waveform_path, event, fig_size, time_range=None):

    # Read the waveform and get the information of it.
    st = read(waveform_path)
    tr = st[0]
    tr.stats.distance = tr.stats.sac['dist'] * 1e3

    fig = plt.figure(figsize=fig_size)
    # get p arrivals and s arrivals
    # eq_o = tr.stats.starttime - tr.stats.sac['b']
    # p_t = eq_o + tr.stats.sac['user9'] - tr.stats.starttime
    # s_t = eq_o + tr.stats.sac['user8'] - tr.stats.starttime

    p_cal = tr.stats.sac['user9']
    s_cal = tr.stats.sac['user8']
    # the time between starttime and p_cal
    p_t = p_cal - tr.stats.sac['b']
    s_t = s_cal - tr.stats.sac['b']

    if time_range == None:
        st.plot(fig=fig, type = 'section', starttime = tr.stats.starttime, endtime = tr.stats.end, 
                orientation='horizontal', linewidth=1.0, show=False)
    else:
        st.plot(fig=fig, type = 'section', starttime = tr.stats.starttime + time_range[0], endtime = tr.stats.starttime + time_range[1], 
                orientation='horizontal', linewidth=1.0, show=False)

    ax = fig.axes[0]
    if time_range == None:
        ax.axvline(p_t, color='blue')
        ax.axvline(s_t, color='red')
    else:
        ax.axvline(p_t - time_range[0], color='blue')
        ax.axvline(s_t - time_range[0], color='red')

    title = '_'.join([event, tr.stats.sac['kstnm'], tr.stats.sac['kcmpnm']])
    plt.title(title)    
    plt.show()


# Plot a list of waveforms
# Ordered of the epicentral distance
def plot_waveform_list(waveform_list, figure_path, title, fig_size, time_range=None, type=None):

    st = Stream()
    for waveform in waveform_list:
        st += read(waveform)

    # get the minimum starttime
    min_start_time = st[0].stats.starttime
    for tr in st:
        tr.stats.distance = tr.stats.sac['dist'] * 1000
        if dtime2int(tr.stats.starttime) <= dtime2int(min_start_time):
            min_start_time = tr.stats.starttime

    # plot the waveform
    fig = plt.figure(figsize=fig_size)
    if time_range != None:
        # time window
        start_time = min_start_time + time_range[0]
        end_time = min_start_time + time_range[1]
        st.plot(type='section', starttime = start_time, endtime = end_time, orientation='horizontal', linewidth=1.0, show=False, fig=fig)
    else:
        st.plot(type='section', orientation='horizontal', linewidth=1.0, show=False, fig=fig)
    
    # label the station, P arrival and S arrival
    ax = fig.axes[0]
    if type == 'cal':
        for i in range(len(st)):
            # get the information of p arrivals and s arrivals
            tr = st[i]
            p_cal = tr.stats.sac['user9']
            s_cal = tr.stats.sac['user8']
            # the time between starttime and p_cal
            p_cal_t = p_cal - tr.stats.sac['b']
            s_cal_t = s_cal - tr.stats.sac['b']

            # the time difference between the start time and min_starttime
            delta_t = tr.stats.starttime - min_start_time
            if time_range != None:
                p_cal_t = p_cal_t + delta_t - time_range[0]
                s_cal_t = s_cal_t + delta_t - time_range[0]
            else:
                p_cal_t = p_cal_t + delta_t
                s_cal_t = s_cal_t + delta_t

            # label the p and s arrivals
            ax.text(p_cal_t, tr.stats.distance / 1e3,  '|', ha='center', color='blue', fontsize=20)
            ax.text(s_cal_t, tr.stats.distance / 1e3,  '|', ha='center', color='red', fontsize=20)
            if len(st) <= 10:
                ax.text(0, tr.stats.sac['dist'], tr.stats.sac['kstnm'], color='red', fontsize=14)
    
    elif type == 'p_pick':
        for i in range(len(st)):
            # get the information of p arrivals and s arrivals
            tr = st[i]
            p_pick = tr.stats.sac['user7']
            # the time between starttime and p_cal
            p_pick_t = p_pick - tr.stats.sac['b']

            # the time difference between the start time and min_starttime
            delta_t = tr.stats.starttime - min_start_time
            if time_range != None:
                p_pick_t = p_pick_t + delta_t - time_range[0]
            else:
                p_pick_t = p_pick_t + delta_t

            # label the p and s arrivals
            ax.text(p_pick_t, tr.stats.distance / 1e3,  '|', ha='center', color='blue', fontsize=20)
            if len(st) <= 10:
                ax.text(0, tr.stats.sac['dist'], tr.stats.sac['kstnm'], color='red', fontsize=14)

    elif type == 'p_pick&cal':
        for i in range(len(st)):
            # get the information of p arrivals and s arrivals
            tr = st[i]
            p_cal = tr.stats.sac['user9']
            p_pick = tr.stats.sac['user7']
            # the time between starttime and p_cal
            p_cal_t = p_cal - tr.stats.sac['b']
            p_pick_t = p_pick - tr.stats.sac['b']          

            # the time difference between the start time and min_starttime
            delta_t = tr.stats.starttime - min_start_time
            if time_range != None:
                p_cal_t = p_cal_t + delta_t - time_range[0]
                p_pick_t = p_pick_t + delta_t - time_range[0]
            else:
                p_cal_t = p_cal_t + delta_t
                p_pick_t = p_pick_t + delta_t

            # label the p and s arrivals
            ax.text(p_cal_t, tr.stats.distance / 1e3,  '|', ha='center', color='blue', fontsize=20)
            ax.text(p_pick_t, tr.stats.distance / 1e3,  '|', ha='center', color='red', fontsize=20)
            if len(st) <= 10:
                ax.text(0, tr.stats.sac['dist'], tr.stats.sac['kstnm'], color='red', fontsize=14)  

    elif type == 'p-s_pick':
        for i in range(len(st)):
            # get the information of p arrivals and s arrivals
            tr = st[i]
            p_pick = tr.stats.sac['user7']
            s_pick = tr.stats.sac['user6']
            # the time between starttime and p_cal
            p_pick_t = p_pick - tr.stats.sac['b']
            s_pick_t = s_pick - tr.stats.sac['b']

            # the time difference between the start time and min_starttime
            delta_t = tr.stats.starttime - min_start_time
            if time_range != None:
                p_pick_t = p_pick_t + delta_t - time_range[0]
                s_pick_t = s_pick_t + delta_t - time_range[0]
            else:
                p_pick_t = p_pick_t + delta_t
                s_pick_t = s_pick_t + delta_t

            # label the p and s arrivals
            ax.text(p_pick_t, tr.stats.distance / 1e3,  '|', ha='center', color='blue', fontsize=20)
            ax.text(s_pick_t, tr.stats.distance / 1e3,  '|', ha='center', color='green', fontsize=20)
            if len(st) <= 10:
                ax.text(0, tr.stats.sac['dist'], tr.stats.sac['kstnm'], color='red', fontsize=14)

    elif type == 'p-s_pick&cal':
        for i in range(len(st)):
            # get the information of p arrivals and s arrivals
            tr = st[i]
            p_cal = tr.stats.sac['user9']
            s_cal = tr.stats.sac['user8']
            p_pick = tr.stats.sac['user7']
            s_pick = tr.stats.sac['user6']
            # the time between starttime and p_cal
            p_cal_t = p_cal - tr.stats.sac['b']
            s_cal_t = s_cal - tr.stats.sac['b']
            p_pick_t = p_pick - tr.stats.sac['b']
            s_pick_t = s_pick - tr.stats.sac['b']            

            # the time difference between the start time and min_starttime
            delta_t = tr.stats.starttime - min_start_time
            if time_range != None:
                p_cal_t = p_cal_t + delta_t - time_range[0]
                s_cal_t = s_cal_t + delta_t - time_range[0]
                p_pick_t = p_pick_t + delta_t - time_range[0]
                s_pick_t = s_pick_t + delta_t - time_range[0]
            else:
                p_cal_t = p_cal_t + delta_t
                s_cal_t = s_cal_t + delta_t
                p_pick_t = p_pick_t + delta_t
                s_pick_t = s_pick_t + delta_t

            # label the p and s arrivals
            ax.text(p_cal_t, tr.stats.distance / 1e3,  '|', ha='center', color='blue', fontsize=20)
            ax.text(s_cal_t, tr.stats.distance / 1e3,  '|', ha='center', color='green', fontsize=20)
            ax.text(p_pick_t, tr.stats.distance / 1e3,  '|', ha='center', color='red', fontsize=20)
            ax.text(s_pick_t, tr.stats.distance / 1e3,  '|', ha='center', color='yellow', fontsize=20)
            if len(st) <= 10:
                ax.text(0, tr.stats.sac['dist'], tr.stats.sac['kstnm'], color='red', fontsize=14)        

    plt.title(title)
    plt.savefig(figure_path)

# Plot functions for manual picks
def plot_waveform_pick(tr_z, tr_n, tr_e, figure_name, pick_type='p'):

    # get the data
    tr_list = [tr_z, tr_n, tr_e]

    if pick_type == 'p-s':
        fig, axes = plt.subplots(3, 1, sharex=True, figsize=(10, 6))

        for i, tr in enumerate(tr_list):

            p_cal = tr.stats.sac['user9']
            s_cal = tr.stats.sac['user8']
            # the time between starttime and p_cal
            p_t = p_cal - tr.stats.sac['b']
            s_t = s_cal - tr.stats.sac['b']
            
            t_max = tr.stats.endtime - tr.stats.starttime
            t = np.linspace(0, t_max, tr.stats.npts)
            data = tr.data

            ax = axes[i]
            ax.plot(t, data, color='black')
            ax.axvline(p_t, color='blue')
            ax.axvline(s_t, color='red')
            ax.set_title(tr.stats.sac['kcmpnm'], color='black', fontsize=10)
            ax.yaxis.set_ticks([])

    elif pick_type == 'p':
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))

        p_cal = tr_z.stats.sac['user9']
        # the time between starttime and p_cal
        p_t = p_cal - tr_z.stats.sac['b']

        t_max = tr_z.stats.endtime - tr_z.stats.starttime
        t = np.linspace(0, t_max, tr_z.stats.npts)
        data = tr_z.data

        ax.plot(t, data, color='black')
        ax.axvline(p_t, color='blue')
        ax.set_title(tr_z.stats.sac['kcmpnm'], color='black', fontsize=10)
        ax.yaxis.set_ticks([])

    plt.xlabel('Time/s', fontsize=12)
    plt.suptitle(figure_name, ha='center', va='top', fontsize=15, color='blue')
    plt.tight_layout()
    # plt.show()
    return fig

