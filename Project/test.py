# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:35:05 2021

@author: Jeanz
"""

from WaitTime import *
from WalkTime import *
from TotalTime import *
from itertools import permutations

waittime_data = WaitTime('Attractions Avg Watingtime (mins).xlsx')
walktime_data = WalkTime('distance_attraction.xlsx')

print(waittime_data.__gettime__(13.4, 2))
print(walktime_data.__gettime__(1, 2))

totaltime_data = TotalTime('Attractions Avg Watingtime (mins).xlsx', 'distance_attraction.xlsx')
print(totaltime_data.__gettime__(12, [0,1,2,3,4,5,6,7]))
print(totaltime_data.__gettime__(12, [0,1,2,3,4,5,7,6]))


## main
attractions = [0, 1, 2, 3, 4, 5, 6, 7]
time_min = 21
time_begin = 12
for p in permutations(attractions):
    time_temp = totaltime_data.__gettime__(time_begin, p)
    if (time_min > time_temp) and (time_temp > 0):
        time_min = time_temp
        p_min = p
        
print(time_min)
print(p_min)