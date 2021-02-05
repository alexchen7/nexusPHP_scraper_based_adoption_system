# -*- coding: utf-8 -*-
import csv
from datetime import datetime
def write_keeper_report(tordic, uid, uname):
    # takes a torrent dict of a keeeper and write in csv
    print ('开始写入保种员', uname, '用户id', uid, '的本月报告')
    
    yy_mm = datetime.now().strftime("%Y_%m")
    
    filename = 'keeper_report_' + yy_mm    
    
    with open(filename, 'a', newline = '', encoding = 'utf-8') as f:
        
        fieldnames = ['用户id', '用户名', '种子id', '种子名', '体积', '做种时间', \
                      '上传量', '同伴数', '第一认领人', '清晰度', '官方', \
                      '更新时间']
        thewriter = csv.DictWriter(f, fieldnames = fieldnames)
        
        for tid in tordic:
            
            tname = tordic[tid]['name']
            size = tordic[tid]['size']
            seedtime = tordic[tid]['time']
            uploads = tordic[tid]['upload']
            seeders = tordic[tid]['seeders']
            firstadopt = tordic[tid]['keeper']
            reso = tordic[tid]['resolution']
            cate = tordic[tid]['official']
            
            thewriter.writerow({'用户id': uid, '用户名': uname, \
                                '种子id': tid, '种子名': tname, \
            '体积': size, '做种时间': seedtime, '上传量': uploads, \
            '同伴数': seeders, '第一认领人': firstadopt, \
            '清晰度': reso, '官方': cate, \
            '更新时间': str(datetime.now())})
    