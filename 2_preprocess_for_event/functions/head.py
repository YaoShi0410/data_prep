"""Functions for modifying the header information of the sac file.
"""
import os
import subprocess
os.putenv("SAC_DISPLAY_COPYRIGHT", '0')

# Reference time
# The only absolute time
# kzdate and kztime can get from these params
def ch_time(fpath, start_time, is_lock=False):
    p = subprocess.Popen(['sac'], stdin=subprocess.PIPE)
    s = "wild echo off \n"
    if is_lock:
        s += "rh %s \n" % (fpath)
        s += "ch lovrok TRUE \n"
        s += "wh \n"
    s += "rh %s \n" % (fpath)
    s += "ch nzyear %s \n" % (start_time.year)
    s += "ch nzjday %s \n" % (start_time.julday)
    s += "ch nzhour %s \n" % (start_time.hour)
    s += "ch nzmin  %s \n" % (start_time.minute)
    s += "ch nzsec  %s \n" % (start_time.second)
    s += "ch nzmsec %s \n" % (int(start_time.microsecond/1e3))
    s += "wh \n"
    s += "q \n"
    p.communicate(s.encode())

# cmpaz (N, E, U) (0, 90, 0)
# cmpinc (N, E, U) (90, 90, 0)
def ch_sta(fpath, knetwk=None, kstnm=None, kcmpnm=None, cmpaz=None, cmpinc=None, stlo=0, stla=0, stel=0):
    p = subprocess.Popen(['sac'], stdin=subprocess.PIPE)
    s = "wild echo off \n"
    s += "rh %s \n" % (fpath)
    s += "ch stlo %s stla %s \n" % (stlo, stla)
    s += "ch stel %s \n" % (stel)
    if knetwk: s += "ch knetwk %s \n" % (knetwk)
    if kstnm:  s += "ch kstnm %s  \n" % (kstnm)
    if kcmpnm: s += "ch kcmpnm %s \n" % (kcmpnm)
    if cmpaz:  s += "ch cmpaz %s  \n" % (cmpaz)
    if cmpinc: s += "ch cmpinc %s \n" % (cmpinc)
    s += "wh \n"
    s += "q \n"
    p.communicate(s.encode())

# Information for event. 
def ch_event(fpath, evlo=None, evla=None, evdp=None, mag=None, o=None):
    p = subprocess.Popen(['sac'], stdin=subprocess.PIPE)
    s = "wild echo off \n"
    s += "rh %s \n" % (fpath)
    if evlo: s += "ch evlo %s \n" % (evlo)
    if evla: s += "ch evla %s \n" % (evla)
    if evdp: s += "ch evdp %s \n" % (evdp)
    if mag: s += "ch mag %s \n" % (mag)
    if o: s += "ch o %s \n" % (o)
    s += "wh \n"
    s += "q \n"
    p.communicate(s.encode())

# Begin time
def ch_b(fpath, b):
    p = subprocess.Popen(['sac'], stdin=subprocess.PIPE)
    s = "wild echo off \n"
    s += "rh %s \n" %(fpath)
    s += "ch b %s \n"%b
    s += "wh \n"
    s += "q \n"
    p.communicate(s.encode())

# add head
def add_pick(fpath, p_cal, s_cal, p_pick, s_pick):
    p = subprocess.Popen(['sac'], stdin=subprocess.PIPE)
    s = "wild echo off \n"
    s += "rh %s \n" % (fpath)
    s += "ch user9 %s \n" % (p_cal)
    s += "ch user8 %s \n" % (s_cal)
    s += "ch user7 %s \n" % (p_pick)
    s += "ch user6 %s \n" % (s_pick)
    s += "wh \n"
    s += "q \n"
    p.communicate(s.encode()) 

