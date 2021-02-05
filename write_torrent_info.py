# -*- coding: utf-8 -*-
import csv
import datetime
def write_torrent_info(tid, tname, reso, category):
    # takes a dict and wrtie to a csv file with torrent id ,name, resolution，
    # and category. need to prevent dup before recording 写入前防重复
    
    # record update time
    update_time = str(datetime.datetime.now().date()) 
    
    with open('torrent_info', 'a', newline = '', encoding = 'utf-8') as f:
        
        fieldnames = ['种子id', '种子名', '清晰度', '官方', '更新时间']
        thewriter = csv.DictWriter(f, fieldnames = fieldnames)
        

        thewriter.writerow({'种子id': tid,'种子名': tname,  \
        '清晰度': reso, '官方': category, '更新时间': update_time})
    
    print ('已写入一条新种子信息')
