import csv
from datetime import datetime
def load_first_adoption():
    # read from the csv file and filter out older records
    
    # create an empty set of torrent ids
    torrent_id = set()
    # create an empty dict of loaded first adoption
    loaded_first_adoption = {}
    
    # open csv file
    with open('first_adoption') as f:
        thereader = csv.reader(f.readlines())
        
        # skip header
        next(thereader)
        
        # loop through every line
        for i in thereader:
            
            # set variable for this torrent id, user id and time
            tid = i[0]
            uid = i[1]
            time = i[2]
            
            # gather data into dictionary
            if tid not in torrent_id:
                
                loaded_first_adoption[tid] = {'uid': uid, 'time': time}
                
                # add torrent_id to set to prevent duplication
                torrent_id.add(tid)
                
            else:
                # set variable for time in current line and dictionary
                i_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
                d_time = datetime.strptime(loaded_first_adoption[tid]['time'], \
                '%Y-%m-%d %H:%M:%S.%f')
                
                # update newer record
                if i_time > d_time:
                    loaded_first_adoption[tid] = {'uid': uid, 'time': time}
                    
                    #print ('csv数据库有重复记录,种子和新第一保种员为', tid, uid)
                    
    return (loaded_first_adoption)