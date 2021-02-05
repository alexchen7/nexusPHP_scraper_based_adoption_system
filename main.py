# -*- coding: utf-8 -*-
from get_keepers import get_keepers
from seeding_stats import seeding_stats

from datetime import datetime
import os.path

from write_keeper_group import write_keeper_group
from load_keeper_report import load_keeper_report
from write_keeper_report import write_keeper_report

def main():
    #create csv file
    
#    with open('output.csv', 'w', encoding = 'utf-8') as csv_file:
#    csvwriter = csv.writer(csv_file, delimiter='\t')
    
#    # load saved torrent info from local
#    loaded_torrent, loaded_torrent_info = load_torrent_info()
#    loaded_adoption, loaded_adoption_info = load_first_adoption()
#    loaded_
    
    # create global variable for loaded_id
    loaded_id = set()
    # variables used for checking if current month's stats were generated
    yr_mo = datetime.now().strftime("%Y_%m")
    file_name_keeper_report = 'keeper_report_' + yr_mo
    
    
    # get finished progress
    if os.path.exists(file_name_keeper_report):
        loaded_id = load_keeper_report()
        print ('上次进度已完成', len(loaded_id), '人')
    
    # get keepers list from website
    keepers_dict = get_keepers()
    
    # write keeper dict to csv file
    write_keeper_group(keepers_dict)
    print ('已生成最新保种组名单')
    
    # num of user being processed
    to_be_done = len(keepers_dict) - len(loaded_id)
    print ('还剩', to_be_done, '人')
    
    current_user = 0
    
    for uid in keepers_dict:
                
        if uid not in loaded_id:
            
            current_user += 1
            print ('正在处理当前第', current_user, '个用户')
            
            user_name = keepers_dict[uid]
            
            # pass uid to seeding stats
            torrent_dict = seeding_stats(uid)
            
            write_keeper_report(torrent_dict, uid, user_name)
            
        print ('完成当前第', current_user, '个用户,还剩', to_be_done - current_user, '人')
        # num of torrent processing for current use
        
        
#        for torrent_id in torrent_dict:
#            # num of detail been recorded
#            current_record = 0
#            current_torrent += 1
#            for stat in torrent_dict[torrent_id]:
#                current_record += 1
#                
#                
#                #csvwriter.writerow([name, keepers_dict[name], torrent_id, stat, torrent_dict[torrent_id][stat]])
#                print('正在处理', name, '第', current_user, '个用户', '第', \
#                      current_torrent, '个种子', '的第', current_record, '条记录')
#    
    
