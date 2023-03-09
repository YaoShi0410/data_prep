"""Convert the format of UTC time to int
"""
from obspy import UTCDateTime

def dtime2str(utc_time):
    date = ''.join(str(utc_time).split('T')[0].split('-'))
    time = ''.join(str(utc_time).split('T')[1].split(':'))[:10]
    time_all = date + time
    str_time = ''.join(time_all.split('.'))

    return str_time

def dtime2int(utc_time):
    int_time = int(dtime2str(utc_time))
    return int_time

def dtime2date(utc_time):
    date = ''.join(str(utc_time.date).split('-'))
    return date

# utc_time = UTCDateTime('20180101')
# print(type(utc_time.julday))
# print(type(dtime2str(utc_time)), type(dtime2int(utc_time)))

# date = ''.join(str(utc_time.date).split('-'))
# year = str(utc_time.year)
# month = str(utc_time.month)
# day = str(utc_time.day)
# hour = str(utc_time.hour)
# minute = str(utc_time.minute)
# second = str(utc_time.second)
# microsecond = str(utc_time.microsecond)

# print(date, year, month, day, hour, minute, second, microsecond)

