# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:36:35 2019

@author: asus
"""

def convert_to_days(dur1):
    # take a duration of the 天:hh:mm:ss format and output days
    
    dur_a = dur1.replace('天', ':')
    
    # set initial duration in seconds
    dur1_sec = 0
    
    # in case HH:MM:SS
    if dur_a.count(':') == 2:
        dur1_sec += int(dur_a[:-6]) * 3600
        dur1_sec += int(dur_a[-5:-3]) * 60
        
    # in case DD:HH:MM:SS
    if dur_a.count(':') == 3:
        dur1_sec += int(dur_a[:-9]) * 86400
        
        dur1_sec += int(dur_a[-8:-6]) * 3600
        
        dur1_sec += int(dur_a[-5:-3]) * 60
            
    # calc seconds
    dur1_sec += int(dur_a[-2:])
    
    # calc days
    dur1_day = round(dur1_sec / 86400, 3)
    
    return dur1_day