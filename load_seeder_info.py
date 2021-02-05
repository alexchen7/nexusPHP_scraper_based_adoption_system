import csv
from datetime import datetime
def load_seeder_info():
    
    torrent_id = set()
    
    loaded_seeder_info = {}
    
    with open('num_seeders') as f:
        
        thereader = csv.reader(f.readlines())
        
        next(thereader)
        
        for i in thereader:
            
            tid = i[0]
            seeders = i[1]
            time = i[2]
            
            if tid not in torrent_id:
                
                loaded_seeder_info[tid] = {'seeders': seeders, 'time': time}
                
                # add torrent_id to set to prevent duplication
                torrent_id.add(tid)
            else:
                # set variable for time in current line and dictionary
                i_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
                d_time = datetime.strptime(loaded_seeder_info[tid]['time'], \
                '%Y-%m-%d %H:%M:%S.%f')
                
                # update newer record
                if i_time > d_time:
                    loaded_seeder_info[tid] = {'seeders': seeders, 'time': time}
                    
    return (loaded_seeder_info)