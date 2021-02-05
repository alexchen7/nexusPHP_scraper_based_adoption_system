# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import re

def current_seeding(user_id):
    # take user id as str and retun a dict of all_seeds

    # Build a dict of the stats of all currently seeding torrents with torrent id,
    # torrent name and number of seeders as keys
    all_seeds = {}
    
    # get web info
    url = 'https://torrent_site.me/getusertorrentlistajax.php?userid=' + user_id + '&type=seeding'
    
    # use your own cookie here
    cookies = 
    all_seeds_page_r = requests.get(url, cookies = cookies)
    all_seeds_page = BeautifulSoup(all_seeds_page_r.text, features = 'lxml')
    
    torrents_info = all_seeds_page.findAll('tr')[1:]
    
    # build dict for all seeding torrents
    for torrent_info in torrents_info:
        # get all a tag
        all_a = torrent_info.findAll('a')
        # get name of torrent
        torrent_name = all_a[1].b.get_text()
        # get torrent id
        torrent_id = all_a[1]['href'][15:-6]
        # grt number of seeders
        num_seeder = torrent_info.findAll('td', \
                    {'align': 'center', 'class': 'rowfollow'})[1].get_text()
        # build dict of seeds
        all_seeds[torrent_id] = {'name': torrent_name, 'seeders': num_seeder}
        
    return (all_seeds)
