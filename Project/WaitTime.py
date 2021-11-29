# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 17:32:17 2021

@author: Jeanz
"""

import pandas as pd
from math import floor

class WaitTime:
    def __init__(self, filename):
        self.name = filename                # name
        self.df = pd.read_excel(filename)
        self.t_start = 12                   # in hour with 24-hours format
        self.t_end   = 21

    def __gettime__(self, time, attactionid):
        
        # check time within time frame
        if (time<self.t_start):
            print("ERROR: time early than start time! ")
            return -1000.0
        elif (time>=self.t_end):
            print("ERROR: time later than end time! ")
            return -1000.0
        
        i_time = floor(time-self.t_start)           # i in the dataframe
        r_time = time - self.t_start - i_time       # remaining time [0,1)
        attaction = "Attraction" + str(attactionid+1)
        wt_start = self.df.loc[i_time, attaction]
        wt_end = self.df.loc[i_time+1, attaction]
        
        wt = wt_start + (wt_end-wt_start)*r_time
        return wt/60.0