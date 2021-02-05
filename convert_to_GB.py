# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 00:15:14 2019

@author: asus
"""

def convert_to_GB(size):
    # intake a str of size and output in MB
    if 'KB' in size:
        size = round(float(size.replace('KB', '')) / (1024 * 1024), 3)
    elif 'MB' in size:
        size = float(size.replace('MB', '')) / 1024
    elif 'GB' in size:
        size = float(size.replace('GB', ''))
    elif 'TB' in size:
        size = float(size.replace('TB', '')) * 1024
    elif 'PB' in size:
        size = float(size.replace('PB', '')) * 1024 * 1024
        
    return size
        