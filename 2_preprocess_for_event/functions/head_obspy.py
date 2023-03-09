"""Functions for modifying the header information of the sac file.
"""

# Reference time
# The only absolute time
# kzdate and kztime can get from these params
def ch_time(tr, start_time, is_lock=False):

    tr.stats.sac['nzyear'] = start_time.year
    tr.stats.sac['nzjday'] = start_time.julday
    tr.stats.sac['nzhour'] = start_time.hour
    tr.stats.sac['nzmin']  = start_time.minute
    tr.stats.sac['nzsec']  = start_time.second
    tr.stats.sac['nzmsec'] = int(start_time.microsecond/1e3)

# cmpaz (N, E, U) (0, 90, 0)
# cmpinc (N, E, U) (90, 90, 0)
def ch_sta(tr, knetwk=None, kstnm=None, kcmpnm=None, cmpaz=None, cmpinc=None, stlo=0, stla=0, stel=0):
    
    tr.stats.sac['knetwk'] = knetwk
    tr.stats.sac['kstnm']  = kstnm
    tr.stats.sac['kcmpnm'] = kcmpnm
    tr.stats.sac['cmpaz']  = cmpaz
    tr.stats.sac['cmpinc'] = cmpinc
    tr.stats.sac['stlo']   = stlo
    tr.stats.sac['stla']   = stla
    tr.stats.sac['stel']   = stel

# Information for event. 
def ch_event(tr, evlo=None, evla=None, evdp=None, mag=None, o=None):

    tr.stats.sac['evlo'] = evlo
    tr.stats.sac['evla'] = evla
    tr.stats.sac['mag']  = mag
    tr.stats.sac['o']    = o

# Begin time
def ch_b(tr, b):
    tr.stats.sac['b'] = b


