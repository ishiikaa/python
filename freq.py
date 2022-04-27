lst = [13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12]
lst2 = [13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14]
lst3 = [13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14, 7]

def frequency(lists):
    dictcount = {}
    minfreq = []
    maxfreq = []
    
    for i in lists:
        count = lists.count(i)
        dictcount.setdefault(i,count)
        
    minval = min(dictcount.values())
    for key, value in dictcount.items():
        if value == minval:
            minfreq.append(key)
    minfreq.sort 
    
    maxval = max(dictcount.values())
    for key, value in dictcount.items():
        if value == maxval:
            maxfreq.append(key)
    maxfreq.sort 
    tuple1 = (minfreq, maxfreq) 
    print(tuple1)
frequency(lst)
frequency(lst2)
frequency(lst3)


    

    
    
        
    
        
