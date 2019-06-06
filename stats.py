import sys
import numpy as np
from datetime import datetime


def min_temp(data_temp):
    fn = sys._getframe().f_code.co_name
    try:
        return min(data_temp, key = lambda t: t[1])
    except TypeError as err:
        raise("{} : The passed variable is either not list or is an empty list {}", fn, err)


def max_temp(data_temp):
    fn = sys._getframe().f_code.co_name
    try:
        return max(data_temp, key=lambda t: t[1])
    except TypeError as err:
        raise ("{} : The passed variable is either not list or is an empty list {}", fn, err)


def mean_temp(data_temp):
    fn = sys._getframe().f_code.co_name
    try:
        temps=[float(d[1]) for d in data_temp]
        return sum(temps)/len(data_temp)
    except TypeError as err:
        raise ("{} : The passed variable is either not list or is an empty list {}", fn, err)


def median_temp(data_temp):
    fn = sys._getframe().f_code.co_name
    try:
        temps = [float(d[1]) for d in data_temp]
        return np.median(np.array(temps))
    except TypeError as err:
        raise ("{} : The passed variable is either not list or is an empty list {}", fn, err)


def warmest_day(data_temp, day_week):

    day0=[]
    for d in data_temp:
        is_day = datetime.strptime(d[0], '%Y-%m-%d %H:%M:%S')
        iso_day = is_day.weekday()
        if iso_day == day_week:
            day0.append(d)
    warmest_day_is = max_temp(day0)
    print("warmest ", (datetime.strptime(warmest_day_is[0], '%Y-%m-%d %H:%M:%S')).strftime("%A"),"with temperature is", warmest_day_is[1])
