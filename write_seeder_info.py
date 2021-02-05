# -*- coding: utf-8 -*-
import csv
import datetime
def write_seeder_info(tid, seeders):
    
    
     with open('num_seeders','a', newline = '') as f:
         
         fieldnames = ['种子id', '做种人数', '更新时间']
         
         thewriter = csv.DictWriter(f, fieldnames = fieldnames)
         
         
         # write in data
         thewriter.writerow({'种子id': tid, \
                             '做种人数':seeders, \
                             '更新时间':str(datetime.datetime.now())})