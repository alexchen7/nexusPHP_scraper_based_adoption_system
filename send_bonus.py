# -*- coding: utf-8 -*-


import requests
import json
from bs4 import BeautifulSoup
import re
from datetime import datetime

def send_bonus(uid, salary):
    # take 2 str of numbers and send bonus
    
    
    url = 'https://torrent_site.me/userdetails.php?id=' + uid
    # use your own cookie here
    cookies = 
    user_profile_r = requests.get(url, cookies = cookies)
    user_profile = BeautifulSoup(user_profile_r.text, features = 'lxml')
    
    # get the form
    form = user_profile.findAll('form', {'method': 'post', 'action': 'modtask.php'})
    
    
    #title = form[0].findAll('td', {'class':'rowfollow', 'valign': 'top', \
    #'align': 'left'})
    
    # get title
    title = form[0].findAll('input', {'type':'text', 'size': '60', \
    'name': 'title'})
    title = str(title[0])
    title = title[title.find('value') + 7: -3]
    
    # get privacy
    privacy = str(form[0].findAll('input', {'type':'radio', 'name': 'privacy', \
    'checked': 'checked'})[0])
    privacy = privacy[privacy.find('value=') + 7: -3]
    
    # get avatar url
    avatar = str(form[0].findAll('input', {'type': 'text', 'size': '60', \
                 'name': 'avatar'}))
    avatar = avatar[avatar.find('value=') + 7: -4]
    
    # get signature
    signature = form[0].findAll('textarea', {'cols': '60', 'rows': '6', \
    'name': 'signature'})
    signature = signature[0].get_text()
    
    # get user class
    u_class = form[0].findAll('select', {'name': 'class'})
    u_class = u_class[0].findAll('option', {'selected': 'selected'})
    u_class = str(u_class[0])
    u_class = u_class[u_class.find('value=') + 7: u_class.find('>')-1]
    #u_class = u_class[find('value'):]
    
    # staff duties
    staff_duties = form[0].findAll('textarea', {'cols': '60', 'rows': '6', \
                       'name': 'staffduties'})
    staff_duties = staff_duties[0].get_text()
    
    # support language
    support_lang = form[0].findAll('input', {'type':'text', 'name':'supportlang'})
    support_lang = str(support_lang[0])
    support_lang = support_lang[support_lang.find('value=') + 7 : -3]
    
    # support
    support = form[0].findAll('input', {'type': 'radio', 'name': 'support', \
                  'checked': 'checked'})
    support = str(support[0])
    support = support[support.find('value=') + 7: -3]
    
    # support_for
    support_for = form[0].findAll('textarea', {'cols': '60', 'rows': '6', \
                      'name': 'supportfor'})
    support_for = support_for[0].get_text()
    
    # movie picker yes or no
    movie_picker = form[0].findAll('input', {'name': 'moviepicker', 'type': 'radio', \
                       'checked' : 'checked'})
    movie_picker = str(movie_picker[0])
    movie_picker = movie_picker[movie_picker.find('value=') + 7: -3]
    
    # reason to be picked as movie_picker
    pick_for = form[0].findAll('textarea', {'cols': '60', 'rows': '6', \
                      'name': 'pickfor'})
    pick_for = pick_for[0].get_text()
    
    # get mod comment
    modcomment = user_profile.findAll('textarea', \
    {'cols':"60", 'name':"modcomment", 'rows':"6"})
    # format mod comment
    modcomment = str(modcomment[0]).replace \
    ('<textarea cols="60" name="modcomment" rows="6">',''). \
    replace('</textarea>', '')
    
    # bonus comment
    bonus_comment = form[0].findAll('textarea', \
    {'cols':"60", 'name':"bonuscomment", 'rows':"6"})
    bonus_comment = bonus_comment[0].get_text()
    
    # warning
    warned = form[0].findAll('table', {'class': 'main', 'cellspacing': '0', \
                  'cellpadding': '5'})
    warned = warned[0]
    warned = str(warned.findAll('td', {'class': 'rowfollow'}))
    warn_pm = ''
    warn_length = '0'
    warning = False
    # use later in form filling
    if '未警告' in warned:
        warning = False
    else:
        warned = 'yes'
        warning = True
        
    # banned or not
    enabled = form[0].findAll('input', {'name': 'enabled', 'checked': 'checked'})
    enabled = str(enabled[0])
    enabled = enabled[enabled.find('value=') + 7: -3]
    
    # forum post allowed?
    forum_post = form[0].findAll('input', {'name': 'forumpost', 'checked': 'checked'})
    forum_post = str(forum_post[0])
    forum_post = forum_post[forum_post.find('value=') + 7: -3]
    
    # upload tor allowed?
    upload_pos = form[0].findAll('input', {'name': 'uploadpos', 'checked': 'checked'})
    upload_pos = str(upload_pos[0])
    upload_pos = upload_pos[upload_pos.find('value=') + 7: -3]
    
    # download tor allowed?
    download_pos = form[0].findAll('input', {'name': 'downloadpos', 'checked': 'checked'})
    download_pos = str(download_pos[0])
    download_pos = download_pos[download_pos.find('value=') + 7: -3]
    
    # no advertisement?
    no_ad = form[0].findAll('input', {'name': 'noad', 'checked': 'checked'})
    no_ad = str(no_ad[0])
    no_ad = no_ad[no_ad.find('value=') + 7: -3]
    
    # no advertisement until: not useful in this case, so set it all 0
    no_ad_until = '0000-00-00 00:00:00'
    
    # user name
    user_name = form[0].findAll('input', {'name': 'username', \
                    'type': 'text', 'size': '25'})
    user_name = str(user_name[0])
    user_name = user_name[user_name.find('value=') + 7: -3]
    
    # user email
    email = form[0].findAll('input', {'name': 'email', \
                    'type': 'text', 'size': '80'})
    email = str(email[0])
    email = email[email.find('value=') + 7: -3]
    
    # turning of secondary auth?
    auth = form[0].findAll('input', {'type': 'radio', 'name': 'turnoffgoogleauth', \
               'checked': 'checked'})
    auth = str(auth[0])
    auth = auth[auth.find('value=') + 7: -3]
    
    # uploaded
    uploaded = form[0].findAll('input', {'name': 'uploaded', \
                    'type': 'text', 'size': '60'})
    uploaded = str(uploaded[0])
    uploaded = uploaded[uploaded.find('value=') + 7: -3]
    
    # downloaded
    downloaded = form[0].findAll('input', {'name': 'downloaded', \
                    'type': 'text', 'size': '60'})
    downloaded = str(downloaded[0])
    downloaded = downloaded[downloaded.find('value=') + 7: -3]
    
    # get the bonus before sending salary
    bonus = form[0].findAll('input', {'name': 'bonus', \
                    'type': 'text', 'size': '60'})
    bonus = str(bonus[0])
    bonus = bonus[bonus.find('value=') + 7: -3]
    
    # number of invites
    invites = form[0].findAll('input', {'type': 'text', 'size': '60', \
                   'name': 'invites'})
    invites = str(invites[0])
    invites = invites[invites.find('value=') + 7: -3]
    
    # bonus after sending salary
    """ONLY FOR NOV 2019 2 x SALARY"""
    
    bonus_aft = round(float(salary) * 2, 1) + round(float(bonus), 1)
    # for my birthday only !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #bonus_aft += 20000
    bonus_aft = str(bonus_aft)
    
    # if in a warning period
    if warning:
        data = {'action': 'edituser',
        'userid': uid,
        'returnto': 'userdetails.php?id=' + uid,
        'title': title,
        'privacy': privacy,
        'avatar': avatar,
        'signature': signature,
        'class': u_class,
        'vip_added': 'no',
        'vip_until': '0000-00-00 00:00:00',
        'staffduties': staff_duties,
        'supportlang': support_lang,
        'support': support,
        'supportfor': support_for,
        'moviepicker': movie_picker,
        'pickfor': pick_for,
        'modcomment':modcomment, 
        'bonuscomment': bonus_comment,
        'warned': warned,
        'enabled': enabled,
        'forumpost': forum_post,
        'uploadpos': upload_pos,
        'downloadpos': download_pos,
        'noad': no_ad,
        'noaduntil': '0000-00-00 00:00:00',
        'username': user_name,
        'email': email,
        'chpassword': '',
        'passagain': '',
        'turnoffgoogleauth': auth,
        'uploaded': uploaded,
        'ori_uploaded': uploaded,
        'downloaded': downloaded,
        'ori_downloaded': downloaded,
        'bonus': bonus_aft,
        'ori_bonus': bonus,
        'invites': invites}
    
    # if not in a warning period    
    else:
        data = {'action': 'edituser',
        'userid': uid,
        'returnto': 'userdetails.php?id=' + uid,
        'title': title,
        'privacy': privacy,
        'avatar': avatar,
        'signature': signature,
        'class': u_class,
        'vip_added': 'no',
        'vip_until': '0000-00-00 00:00:00',
        'staffduties': staff_duties,
        'supportlang': support_lang,
        'support': support,
        'supportfor': support_for,
        'moviepicker': movie_picker,
        'pickfor': pick_for,
        'modcomment':modcomment, 
        'bonuscomment': bonus_comment,
        'warnlength': warn_length,
        'warnpm': warn_pm,
        'enabled': enabled,
        'forumpost': forum_post,
        'uploadpos': upload_pos,
        'downloadpos': download_pos,
        'noad': no_ad,
        'noaduntil': '0000-00-00 00:00:00',
        'username': user_name,
        'email': email,
        'chpassword': '',
        'passagain': '',
        'turnoffgoogleauth': auth,
        'uploaded': uploaded,
        'ori_uploaded': uploaded,
        'downloaded': downloaded,
        'ori_downloaded': downloaded,
        'bonus': bonus_aft,
        'ori_bonus': bonus,
        'invites': invites}
    
    r = requests.post("https://hdsky.me/modtask.php", cookies = cookies, data = data)