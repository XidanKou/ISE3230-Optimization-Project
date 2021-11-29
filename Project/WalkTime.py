# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 19:05:55 2021

@author: Jeanz
"""

import pandas as pd

class WalkTime:
    def __init__(self, filename):
        self.name = filename
        self.df = pd.read_excel(filename, header = 0)
        
    def __gettime__(self, i, j):
        attractionj = "Attraction" + str(j+1)
        return self.df.at[i,attractionj]/60.0
        