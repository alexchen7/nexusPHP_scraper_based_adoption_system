import csv
import datetime
def write_keeper_group(keeper_dict):
    # takes a dict and wrtie to a csv file with keepers' id, name and time   
    
    # record current time
    update_time = str(datetime.datetime.now().date())
    filename = 'keeper_list_' + str(datetime.datetime.now().date()).replace("-","_")
    
    # creates a file with name based on current date
    with open(filename,'w', newline = '') as f:
        fieldnames = ['保种员id', '用户名', '更新时间']
        thewriter = csv.DictWriter(f, fieldnames = fieldnames)
        thewriter.writeheader()
        
        # looping the input dict
        for keeper_id in keeper_dict:
            
            keeper_name = keeper_dict[keeper_id]
            
            # record information
            thewriter.writerow({'保种员id':keeper_id, \
                                '用户名':keeper_dict[keeper_id], \
                                '更新时间':update_time})
    print ('完成记录本月全部保种员名单')