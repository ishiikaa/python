lst = [13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12]
lst2 = [13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14]
lst3 = [13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14, 7]

#dictcount = {13:4,12:2,11:2,14:2,7:1}
def frequency(lst):
    dictcount = {}
    minfreq = []
    maxfreq = []
    for i in lst:
        count = lst.count(i)
        dictcount.setdefault(i, count)

    minval = min(dictcount.values())
    for k, v in dictcount.items(): 
        if v == minval:
            minfreq.append(k)
    minfreq.sort()

    maxval = max(dictcount.values())
    for k, v in dictcount.items():
        if v == maxval:
            maxfreq.append(k)
    maxfreq.sort() 
    tup1 = (minfreq, maxfreq)
    print(tup1)


frequency(lst)
frequency(lst2)
frequency(lst3)