# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:55:44 2019

@author: asus
"""

import requests
import json
from bs4 import BeautifulSoup
import re
from datetime import datetime
import csv
import math
from convert_to_days import convert_to_days
from convert_to_GB import convert_to_GB
from write_salary_report import write_salary_report
from write_seedtime import write_seedtime
from load_seedtime import load_seedtime
from tqdm import tqdm

def salary_calc():
    # open up keeper report and calc bonus points
    
    yy_mm = datetime.now().strftime("%Y_%m")
    filename = 'keeper_report_' + yy_mm
    
    
    f = csv.DictReader(open(filename, encoding="utf-8"))
    
    # make a blank keeper report dict
    keeper_report = {}
    
    # these keepers get 0 salary
    zero_salary = set()
    
    # open up keeper_report line by line
    print ('正在读取做种信息...')
    for i in f:
        
        # should
        user_id = i['用户id']
        user_name = i['用户名']
        torrent_id = i['种子id']
        torrent_name = i['种子名']
        size = i['体积']
        seed_time = i['做种时间']
        uploaded = i['上传量']
        peers = i['同伴数']
        first_adopted = i['第一认领人']
        resolution = i['清晰度']
        official = i['官方']
        date = i['更新时间']
        
        # in case this uid is in the dic
        if user_id in keeper_report:
            keeper_report[user_id]['做种情况'][torrent_id] = \
            {'种子名': torrent_name, '体积': size, '做种时间': seed_time, \
             '上传量': uploaded, '同伴数': peers, '第一认领人': first_adopted, \
             '清晰度': resolution, '官方': official, '更新时间': date}
            
        # in case this uid is not in the dic
        else:
            keeper_report[user_id] = {'用户名': user_name, '做种情况':{}}
            keeper_report[user_id]['做种情况'][torrent_id] = \
            {'种子名': torrent_name, '体积': size, '做种时间': seed_time, \
             '上传量': uploaded, '同伴数': peers, '第一认领人': first_adopted, \
             '清晰度': resolution, '官方': official, '更新时间': date}
            
    print ('信息读取完毕,正在判断未达标保种员')
    
   
            
    for i in tqdm(keeper_report):
        
        # initialize number of torrents satisfied for bonus
        num_satisfied = 0
        
        # identifying keepers with zero salary
        if (len(keeper_report[i]['做种情况'])) < 100:
            zero_salary.add(i)
            #print (i, keeper_report[i]['用户名'],'7月的认领数量', len(keeper_report[i]['做种情况']))
            
        
        for j in keeper_report[i]['做种情况']:
            
            # select torrents with seeding time shorter than 9.5 days
            if convert_to_days( \
            keeper_report[i]['做种情况'][j]['做种时间']) >= 9:
#                print ('seeding time ok')
                # check if the torrent is official
                if keeper_report[i]['做种情况'][j]['官方'] == '1':
                    #print ('pass offcial check ok')
                    # check if the keeper is the first adopter
                    if keeper_report[i]['做种情况'][j]['第一认领人'] == i:
                        #print ('first adption ok')
                        # check if the torrent is larger than 1GB
                        if convert_to_GB( \
                        keeper_report[i]['做种情况'][j]['体积']) >= 0.99:
                            #print ('size ok')
                            # add to num of satisfied torrents
                            num_satisfied += 1

        # record keepers with less than 100 qualified torrents
        if num_satisfied < 100:
            zero_salary.add(i)
            
    print ('未达标保种员分析完毕,准备更新做种时间')
    
    # write seeding time to database
    write_seedtime(keeper_report, zero_salary)
    
    # load saved seedtime info
    loaded_seedtime = load_seedtime()
    
    # calculating bonus
    for i in keeper_report:
        for j in keeper_report[i]['做种情况']:
            
            size = convert_to_GB(keeper_report[i]['做种情况'][j]['体积'])
            
            # seedtime needs to pull up from database做种时间需要从数据库提取！！已经更改
            seedtime = float(loaded_seedtime[i][j])
            
            # add total seedtime to the dic
            keeper_report[i]['做种情况'][j]['总做种时间'] = \
            float(loaded_seedtime[i][j])
            
            peers = int(keeper_report[i]['做种情况'][j]['同伴数'])
            # prevents zero division. happens when keeper is offline during data
            # collection and no one is seeding
            if peers == 0:
                peers = 1

            uploads = convert_to_GB(keeper_report[i]['做种情况'][j]['上传量'])
            
            # calculate salary for one torrent
            salary = round(100 * size * (0.25 + (0.6 * math.log(1 + seedtime) \
            / (peers**0.6))) + 20 * uploads, 3)
            
            # in case the torrent didn't satisfy the requirement, set salary=0
            if (keeper_report[i]['做种情况'][j]['官方'] != '1') or \
            (convert_to_days( \
            keeper_report[i]['做种情况'][j]['做种时间']) < 9) or \
            (keeper_report[i]['做种情况'][j]['第一认领人'] != i) or \
            (convert_to_GB( \
                        keeper_report[i]['做种情况'][j]['体积']) < 0.99):
                salary = 0
                
            # record the reward for the torrent    
            keeper_report[i]['做种情况'][j]['单种魔力'] = salary
            
    

    # write the csv salary form for publication
    write_salary_report(keeper_report, zero_salary)
    
    return zero_salary, keeper_report
    
    #for i in keeper_report:
            
    