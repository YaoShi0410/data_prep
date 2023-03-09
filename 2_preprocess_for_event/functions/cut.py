"""Cut traces by Obspy trim.
"""
from obspy import read, UTCDateTime

# Cut the trace between [start_time, end_time]
# tr is obspy.core.trace.Trace, start_time and end_time are both UTCDateTime
def cut(tr, start_time, end_time, pad=True, nearest_sample=True, fill_value=float):

    tr.trim(start_time, end_time, pad, nearest_sample, fill_value)
    
    return tr

# st = read('./test/1002_20210922204856_.9800000.EHN.SAC')
# tr = st[0]
# print(tr.stats.npts)

# start_time = UTCDateTime('2021092314555')
# end_time = UTCDateTime('2021092315055')

# tr = cut(tr, start_time, end_time)
# print(tr.stats.npts)