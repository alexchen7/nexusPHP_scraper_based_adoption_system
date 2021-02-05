# -*- coding: utf-8 -*-
import csv
from datetime import datetime
from tqdm import tqdm

def write_salary_report(salary_report, zero_salary):
    # takes dict of keeper report which contains uid as primary key, and
    # seeding stats as a secondary key.  teritary key is torrent id.
    # also takes a set of keeper ids with 0 salary
    
    # get time for file name
    yy_mm = datetime.now().strftime("%Y_%m")
    # concat time with file name header
    filename = 'salary_report_' + yy_mm
    
    # initialize total salary per keeper
    total_salary = 0
    
    # initialize assesment value pass = 1 fail = 0
    assessment = 0
    
    # create a global variable for date
    date = ''
    
    # flag for wrtie field name
    write_fieldname = True
    
    for i in tqdm(salary_report):
        
        
        
        with open(filename, 'a', newline = '', encoding = 'utf-8') as f:
            
            
            fieldnames = ['用户id', '用户名', '种子id', '种子名', '体积', '做种时间', \
                          '上传量', '同伴数', '第一认领人', '清晰度', '官方', \
                          '总做种时间', '单种魔力', '总魔力', '达标', '更新时间']
            
            thewriter = csv.DictWriter(f, fieldnames = fieldnames)
            
            # write filedname for the first time
            if write_fieldname:
                thewriter.writeheader()
                write_fieldname = False
                
            
            for j in salary_report[i]['做种情况']:
                
                uid = i
                uname = salary_report[i]['用户名']
                tname = salary_report[i]['做种情况'][j]['种子名']
                tid = j
                size = salary_report[i]['做种情况'][j]['体积']
                seedtime = salary_report[i]['做种情况'][j]['做种时间']
                # 待更改！！建库要更改！！！！！！！！已更改！
                total_seedtime = salary_report[i]['做种情况'][j]['总做种时间']
                uploads = salary_report[i]['做种情况'][j]['上传量']
                seeders = salary_report[i]['做种情况'][j]['同伴数']
                firstadopt = salary_report[i]['做种情况'][j]['第一认领人']
                reso = salary_report[i]['做种情况'][j]['清晰度']
                cate = salary_report[i]['做种情况'][j]['官方']
                date = salary_report[i]['做种情况'][j]['更新时间']
                salary_per_tor = salary_report[i]['做种情况'][j]['单种魔力']
                
                
                thewriter.writerow({'用户id': uid, '用户名': uname, \
                                    '种子id': tid, '种子名': tname, \
                '体积': size, '做种时间': seedtime, '上传量': uploads, \
                '同伴数': seeders, '第一认领人': firstadopt, \
                '清晰度': reso, '官方': cate, '总做种时间': total_seedtime, \
                '单种魔力': salary_per_tor, '更新时间': date})
                
                # add to keeper's total salary
                total_salary += salary_per_tor
            
            # set total salary 0 for keepers in zero salary
            if i in zero_salary:
                total_salary = 0
                assessment = 0
            else:
                assessment = 1
            
            # prepare uid, uname, date, to write
            uid = i
            uname = salary_report[i]['用户名']
            # write the total salary for the keeper
            thewriter.writerow({'用户id': uid, '用户名': uname, \
            '总魔力': total_salary, '达标': assessment, '更新时间': date})
            
            # reset total salary
            total_salary = 0
            
    print ('工资表格写入完成')