import csv
import datetime
def write_first_adoption(tid, first_keeper):
    # Write the torrent id and first people adopted.第一做种人表格。
    # updates are differeniated by 更新时间        
    
    # open up the file and make changes
    with open('first_adoption','a', newline = '') as f:
        
        fieldnames = ['种子id', '第一认领者', '更新时间']
        
        thewriter = csv.DictWriter(f, fieldnames = fieldnames)   
        
        # write in data
        thewriter.writerow({'种子id': tid, \
        '第一认领者':first_keeper, '更新时间':str(datetime.datetime.now())})
                
                