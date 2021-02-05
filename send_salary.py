# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import re
import csv
from send_bonus import send_bonus
import os.path
from tqdm import tqdm
from datetime import datetime

##文件名全部没有通用性，已发列表需要改进添加更新日期到日期

#要使用检测文件是否存在功能来判断是否建库

def send_salary():
    # take a csv file and call send bonus to do action
    
    yy_mm = datetime.now().strftime("%Y_%m")
    filename = 'salary_report_' + yy_mm

    # create global variable for progress in previous session
    loaded_sent_salary = set()
    
    # check the progress and record in loaded_sent_salary
    f = csv.DictReader(open('已发工资'))
    
    for i in f:
        loaded_sent_salary.add(i['uid'])
        
    
    loaded_report = {}
    
    g = csv.DictReader(open(filename, encoding="utf-8"))
    
    for i in g:
        
        if i['总魔力']:
            if i['用户id'] not in loaded_sent_salary and float(i['总魔力']) != 0:
                loaded_report[i['用户id']] = i['总魔力']
    
    

        
        

    with open('已发工资', 'a', newline = '') as f:
        
        fieldnames = ['uid']
        
        
        thewriter = csv.DictWriter(f, fieldnames = fieldnames)
        
        thewriter.writeheader()
        
        for i in tqdm(loaded_report):
        
            send_bonus(i, loaded_report[i])
            
            thewriter.writerow({'uid': i})
                
        
        