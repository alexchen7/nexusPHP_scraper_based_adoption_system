# -*- coding: utf-8 -*-
import csv
def load_torrent_info():
    # It loads the torrent_info.csv then create a set of torrent id stored in
    # it. It returns a set of torrents and a dict with torrent info.
    
    # create an empty set of loaded torrents
    torrent_loaded = set()
    # create an empty dict of torrent info
    torrent_info = {}
    
    # opens the csv file
    f = csv.DictReader(open("torrent_info", encoding = 'utf-8'))
    
    # loop through lines in csv
    for i in f:
        # add to set
        torrent_loaded.add(i['种子id'])
        # add to the dict
        torrent_info[i['种子id']] = {'种子名':i['种子名'], '清晰度':i['清晰度'], \
                    '官方':i['官方'], '更新时间':i['更新时间']}
        
    return (torrent_info)