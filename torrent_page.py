import requests
import json
from bs4 import BeautifulSoup
import re
#from write_first_adopton import write_first_adoption

def keepers_official(torrent_id):
    # take torrent_id and return list of keepers and official category or not
    # returns num_seeders, list of keepers, category, resolution

    # list of keepers' name and uid for this torrent
    keeper_list = []
    keeper_id = []
    # set initial value 0 as non-official
    official = 0
    # set resolution to blank str
    resolution = ''
    
    # get web info
    url = "https://torrent_site.me/details.php?id=" + torrent_id + "&hit=1"
    # use your own cookie here
    cookies = 
    torrent_page_r = requests.get(url, cookies = cookies)
    torrent_page = BeautifulSoup(torrent_page_r.text, features = 'lxml')
    
    # number of seeders for this torrent
    peer_info = torrent_page.findAll('div', {'id':'peercount'})
    num_seeders = re.sub("[^0-9]", "", peer_info[0].b.get_text())
     
    #get category table
    category_table = torrent_page.findAll('td', \
    {'class':'rowfollow', 'valign':'top','align':'left'})
    
    # get category and resolution information   
    for i in category_table:
        if "制作组:" in i.text:
            # get position of category
            group_name_position = i.text.find('制作组') + 5
            # get position of resolution
            resolution_position = i.text.find("分辨率") + 5
            # get resolution
            resolution = i.text[resolution_position: group_name_position-8]
            # get category
            if 'HDS' in i.text[group_name_position:]:
                official = 1
                break
            else:
                break

    # get all td forms
    all_td = torrent_page.findAll('td', {'class':'rowfollow', \
                                         'valign':'top', 'align':'left'})
    
    # iterate through all_td to get adoption table
    for i in all_td:
        # get adtoption table
        if '目前认领该种子的用户' in i.get_text():
            # get keepers' info into a list
            keepers = (i.findAll('a', {'class' : 'Keeper_Name'}))
            
            # get name of individual keeper and build in keeper_list
            for keeper in keepers:
                # get uid
                keeper_id.append(str(keeper)[str(keeper).find('php?') + 7:str(keeper).find("<b>") - 2])
                # get keeper's name
                keeper_list.append(keeper.b.get_text())
                
    # in case keeper_list is 0
    if len(keeper_list) == 0:
        keeper_list.append('0')
        keeper_id.append('0')
    

                
    return (num_seeders, keeper_list, official, resolution, keeper_id)
