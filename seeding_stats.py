# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import re
from return_shorter_duration import return_shorter_duration
from torrent_page import keepers_official
from all_seeds_page import current_seeding

from write_torrent_info import write_torrent_info
from write_first_adoption import write_first_adoption
from write_seeder_info import write_seeder_info
from load_seeder_info import load_seeder_info
from load_torrent_info import load_torrent_info
from load_first_adoption import load_first_adoption

def seeding_stats(user_id):
    # Get str of user_id and return a dict of adopted with fact of 
    #torrent info (name, id, size, seeding time, num_seeder, keepers, uploads,
    # resolution, cate) as values.
    
    # set initial value for dict不确定是否需要
    seeders = ''
    keepers = []
    official = 0
    resolution = ''
    keeper_id = []

    # create an empty set to store torrent_id and prevent duplication
    torrent_set = set()
    
    # get seeders info from all_seeding page抓取全部做种信息
    print ('从做种页面抓取信息中...')
    all_seeding = current_seeding(user_id)
    print ('抓取完毕')
    # load all saved torrent_info
    print ('从数据库加载信息中...')
    loaded_tor_info = load_torrent_info()
    loaded_adop_info = load_first_adoption()
    loaded_seeder_info = load_seeder_info()
    print ('数据库信息已加载')
    
    # create a dict of torrents
    torrent_dict = {}
    # get web info
    inofficial_count = 0
    url = 'https://torrent_site.me/getusertorrentlistajax.php?userid=' + user_id +'&type=adoption'
    # use your own cookie
    cookies = 
    user_profile_r = requests.get(url, cookies = cookies)
    user_profile = BeautifulSoup(user_profile_r.text, features = 'lxml')
    
    # get info for every torrent, skip first line
    torrents_info = user_profile.findAll('tr')[1:]
    
    progress = 0
    
    # build dict for seeding stats
    for torrent_info in torrents_info:        
        all_a = torrent_info.findAll('a')
        
        progress += 1
        print ('正在加载第', progress, '个种子入', user_id,'的种子字典')
        
        # get torrent name
        torrent_name = all_a[1].b.get_text()
        
        # get torrenrt id
        torrent_id = all_a[1]['href'][15:-6]
        
        #### get info in csv？？？？？？？？？？？？以前写的
        #if i not in 
        
        
        # find seeding time which locates at the third 'td' tag
        seeding_time = torrent_info.findAll('td', \
                        {'align':"center", 'class':"rowfollow"})[2].get_text()
        
        # get torrent size
        torrent_size = torrent_info.findAll('td', \
                        {'align':"center", 'class':"rowfollow"})[0].get_text()
        
        # get upload data info for torrent
        torrent_upload = torrent_info.findAll('td', {'align':"center", \
                     'class':"rowfollow"})[1].get_text()        

        # allow only new torrent in dict
        if torrent_id not in torrent_set:
            torrent_dict[torrent_id] = {'size': torrent_size, \
                         'time': seeding_time, 'name': torrent_name, \
                         'upload': torrent_upload, 'seeders': '', \
                         'keeper': '', 'resolution': '', 'official': ''}
            
            # prevents null error, write seeders in dict
            if torrent_id in all_seeding:
                # get torrent seeders from the all seeding torrents page
                seeders = all_seeding[torrent_id]['seeders']
                torrent_dict[torrent_id]['seeders'] = seeders
                print ('成功从个人做种页面获取到了', torrent_id, '的做种人数')
                
            if not torrent_dict[torrent_id]['seeders']:
                print ('未能从个人做种页面获取到', torrent_id, '的做种人数，尝试本地数据库。')
                if torrent_id in loaded_seeder_info:
                    seeders = loaded_seeder_info[torrent_id]['seeders']
                    torrent_dict[torrent_id]['seeders'] = seeders
                    print ('成功从本地数据库获取到', torrent_id, "的信息并加入字典")
                else:
                    print ('本地数据库没有', torrent_id, '的做种人数信息')
            
            # pull data from data base: torrent info of reso and cate
            if torrent_id in loaded_tor_info:
                reso, cate = loaded_tor_info[torrent_id]['清晰度'], loaded_tor_info[torrent_id]['官方']
                torrent_dict[torrent_id]['resolution'] = reso
                torrent_dict[torrent_id]['official'] = cate
                print ('已从数据库中加载', torrent_id, '的分辨率和分类信息')
            else:
                print ('数据库没有种子', torrent_id, '的分辨率和分类信息')
                
            # pull data from data base: first adoption    
            if torrent_id in loaded_adop_info and (loaded_adop_info[torrent_id]['uid'] == user_id):
                
                keeper = loaded_adop_info[torrent_id]['uid']
                torrent_dict[torrent_id]['keeper'] = keeper
                print ('已从数据库加载', torrent_id, '的第一做种人信息')
            else:
                print ('数据库没有种子', torrent_id, '的第一做种人信息')
                
        # update torrent_dict with shorter seeding_time
        else:
            torrent_dict[torrent_id]['time'] = return_shorter_duration(torrent_dict[torrent_id]['time'], seeding_time)
            
        # build set of torrent
        torrent_set.add(torrent_id)
    print ( user_id, '的', progress, '个种子已装入字典')
        # getting stats for num_seeders and category
    progress = 0
    
    # get and record num_of seeders, keepers, official, resolution information
    
    for i in torrent_dict:

        progress += 1
        
        print ('正在处理', user_id, '的字典中的第', progress, '个种子')
        
        
        
        # need to update per info, default true.便于记忆是否访问过
        update_adoption = True
        update_seeders = True
        
        #此处为读取csv数据库的命令
        print ('再次加载种子信息库以及种子认领库')
        loaded_torrent_info = load_torrent_info()
        loaded_adoption_info = load_first_adoption()
        loaded_seeders = load_seeder_info()
        
        
        # if torrent in adoption table not in saved in torrent_info, write it 
        # in. 写入没有存储的种子信息。为了避免重复访问，同时应对各类情况，有3个if，
        # 暂时未能找到更好的解决办法
        if i not in loaded_torrent_info:
            print ('种子不在种子信息数据库中,现在获取')
            # go to torrent page and get all detailed info
            seeders, keepers, official, resolution, keeper_id = keepers_official(i)
            
            torrent_dict[i]['seeders'] = seeders
            torrent_dict[i]['keeper'] = keeper_id[0]
            torrent_dict[i]['official'] = official
            torrent_dict[i]['resolution'] = resolution            
            write_torrent_info(i, torrent_dict[i]['name'].replace(',',''), resolution, official)
            print ('完成一次写入种子信息数据库')            
        
            # write first keeper adopted the torrent into csv if not present or
            # keeper doesn't match
            if i not in loaded_adoption_info or (loaded_adoption_info[i]['uid'] != keeper_id[0]):
                # write into first adoption csv
                write_first_adoption(i, keeper_id[0])
                print ('完成一次写入到第一认领人数据库')
                # update flag
                update_adoption = False
                
            if i not in loaded_seeders:
                write_seeder_info(i, seeders)
                print ('完成一次写入到做种人数数据库')
                update_seeders = False
                
        if update_adoption and (i not in loaded_adoption_info or (loaded_adoption_info[i]['uid'] != user_id)):
            
            seeders, keepers, official, resolution, keeper_id = keepers_official(i)
            torrent_dict[i]['seeders'] = seeders
            torrent_dict[i]['keeper'] = keeper_id[0]
            torrent_dict[i]['official'] = official
            torrent_dict[i]['resolution'] = resolution
            
            write_first_adoption(i, keeper_id[0])
            print ('完成一次写入到第一认领者数据库。...有特殊情况,可能是因为换种或新认领，有种子信息，但没认领信息')
            
            if update_seeders and (i not in loaded_seeders):
                write_seeder_info(i, seeders)
                update_seeders = False
                print ('完成一次写入到做种人数数据库。...有特殊情况，可能是因为换种或新认领,有种子信息，但没认领信息和做种数信息')
        
        if update_seeders and (i not in loaded_seeders):
            # check if seeders are actually in dict
            if torrent_dict[i]['seeders']:
                write_seeder_info(i, torrent_dict[i]['seeders'])
                print ('完成一次写入到做种人数数据库。...有特殊情况，可能是因为换种或新认领,有种子信息，有认领信息但没做种数信息')
            else:
                seeders, keepers, official, resolution, keeper_id = keepers_official(i)
                write_seeder_info(i, seeders)
                print ('完成一次写入到做种人数数据库。...有特殊情况，可能是因为换种或新认领,有种子信息，有认领信息但没做种数信息')
            
        print ('处理完毕', user_id, '的第', progress, '个种子')
            
            
            
            
            
        
#        # report more than 1 keepers
#        if len(keepers) > 1:
#            print ('保种员>1,有', \
#                   keepers[:], '在保', torrent_dict[i]['name'], 'id为', i)
#            
#        # report unofficial category
#        if official < 1:
#            inofficial_count += 1
#            print (i, torrent_dict[i]['name'], '非官方种子数', inofficial_count)
#            
#        # report 720p low resolution
#        if '720p' in resolution:
#            print (i, torrent_dict[i]['name'], '为720p', '请换种')
#            
#        # progress report
#        progress += 1
#        print ('正在扫描用户' + user_id + '的第' + str(progress) + '个种子')
    
    print ('用户', user_id, '共', progress, '个种子处理完毕')
    return (torrent_dict)
        