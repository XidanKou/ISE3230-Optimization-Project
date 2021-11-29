# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 19:01:07 2021

@author: Jeanz
"""

from WaitTime import *
from WalkTime import *

class TotalTime:
    def __init__(self, filename1, filename2):
        self.name1 = filename1                # name
        self.name2 = filename2                # name
        self.waittime_data = WaitTime(filename1)
        self.walktime_data = WalkTime(filename2)
    def __gettime__(self, time, alist):
        num = len(alist)
        current_time = time
        
        # wait time @ 1st attaction
        self.waittime_data.__gettime__(current_time, alist[0])
        
        for i in range(num-1):
            j = i
            k = i+1
            walk_time = self.walktime_data.__gettime__(alist[j], alist[k])
            current_time = current_time + walk_time
            wait_time = self.waittime_data.__gettime__(current_time, alist[k])
            current_time = current_time + wait_time
            if (wait_time < 0):
                return wait_time
            
        return current_time
