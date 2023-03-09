from obspy import read, UTCDateTime
from obspy.taup import TauPyModel
import numpy as np
import matplotlib.pyplot as plt

model = TauPyModel(model="ak135")

st = read('./waveform_data/20210923070050000_1.60/1001_20210923070050000_1.60_EHE.SAC')
# st1 = read('./events_data_cal_10+60s/AEJ_2/1001_20210925175236_.9790000.EHN.SAC')
# st2 = read('./events_data_cal_10+60s/AEJ_2/1001_20210925175236_.9790000.EHZ.SAC')
tr = st[0]
print(tr.stats.starttime - tr.stats.sac['b'], tr.stats.sampling_rate==100.0)
# tr1 = st1[0]
# tr2 = st2[0]
# dist = tr.stats.sac['gcarc']
# dep = tr.stats.sac['evdp']
# print(type(tr.stats.sac['kstnm']), type(tr.stats.sac['kcmpnm']), tr.stats.sac['nzjday'], tr.stats.sac['nzsec'], tr.stats.npts)
# print(tr.stats.starttime, tr.stats.endtime)
# print(tr.data, type(tr.data), tr.data.shape)

# # print(dist, dep)
# p_arrivals = model.get_travel_times(source_depth_in_km=10, 
#                                     distance_in_degree=3.6, phase_list=['P', 'Pn', 'Pg', 'p', 'Pdiff']) 

# # get the first arrival time of p wave
# p_arr_list = []
# for i in range(len(p_arrivals)):
#     p_t = p_arrivals[i].time
#     p_arr_list.append(p_t)

# p_arr = min(p_arr_list)

# s_arrivals =  model.get_travel_times(source_depth_in_km=10, 
#                                     distance_in_degree=3.6, phase_list=['S', 'Sn', 'Sg', 's', 'Sdiff'])          

# # get the first arrival time of p wave
# s_arr_list = []
# for i in range(len(s_arrivals)):
#     s_t = s_arrivals[i].time
#     s_arr_list.append(s_t)

# s_arr = min(s_arr_list)

# print(p_arrivals, s_arrivals, p_arr, s_arr, s_arr - p_arr)
# # print(tr.stats.sac['gcarc'])
# # print(tr.stats.starttime, tr.stats.endtime)
# data = tr.data
# t_range = tr.stats.endtime - tr.stats.starttime
# t = np.linspace(0, t_range, tr.stats.npts)
# plt.figure(figsize=(10, 4))
# plt.plot(t, data, 'black')
# plt.axvline(p_arr, color='blue')
# plt.axvline(s_arr, color='red')
# plt.show()

# tr.plot()
# tr.stats.starttime = UTCDateTime('20190101')

# tr.write('./1A.NE24.20080101000000.00.BHE.mseed')
# print(tr.stats.starttime, tr.stats.endtime)
# print(tr.stats.sac['gcarc'])
# tr.stats.sac['b'] = 0
# t0 = UTCDateTime('20180101125825')
# t1 = UTCDateTime('20180101125624')

# print(t0, t1, t0-t1)

# tr = read('./test.sac')[0]
# tr1 = read('./test01.sac')[0]
# tr2 = read('./test02.sac')[0]

# print(tr.stats.starttime, tr.stats.station, tr.stats.network, tr.stats.channel, tr.stats.location, tr.stats.endtime)
# print(tr1.stats.starttime, tr1.stats.station, tr1.stats.network, tr1.stats.channel, tr1.stats.location, tr.stats.endtime)
# print(tr2.stats.starttime, tr2.stats.station, tr2.stats.network, tr2.stats.channel, tr2.stats.location, tr.stats.endtime)
