def return_shorter_duration( dur1, dur2):
# take 2 strs of duration and return the shorter one  
    dur_a = dur1.replace('天', ':')
    dur_b = dur2.replace('天', ':')
    # set initial duration in seconds
    dur1_sec = 0
    dur2_sec = 0
    # in case HH:MM:SS
    if dur_a.count(':') == 2:
        dur1_sec += int(dur_a[:-6]) * 3600
        dur1_sec += int(dur_a[-5:-3]) * 60
    if dur_b.count(':') == 2:
        dur2_sec += int(dur_b[:-6]) * 3600
        dur2_sec += int(dur_b[-5:-3]) * 60
        
    # in case DD:HH:MM:SS
    if dur_a.count(':') == 3:
        dur1_sec += int(dur_a[:-9]) * 86400
        dur1_sec += int(dur_a[-8:-6]) * 3600
        dur1_sec += int(dur_a[-5:-3]) * 60
        
    if dur_b.count(':') == 3:
        dur2_sec += int(dur_b[:-9]) * 86400
        dur2_sec += int(dur_b[-8:-6]) * 3600
        dur2_sec += int(dur_b[-5:-3]) * 60
    # calc seconds
    dur1_sec += int(dur_a[-2:])
    dur2_sec += int(dur_b[-2:])
    
    # return shorter one
    if dur1_sec < dur2_sec:
        return dur1
    else:
        return dur2