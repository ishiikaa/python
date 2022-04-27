def expanding(list1):
    lst1 = []
    flag = 0
    a = len(list1)
    for i in range(0,a):
       if(i == a - 1):
           break
       diff = abs(list1[i]-list1[i+1])
       lst1.append(diff)
    print(lst1)
    
    b = len(lst1)
    for i in range(0,b):
        if(i == b - 1):
            break
        if(lst1[i] < lst1[i+1]):
            flag = 1
        else:
            flag = 0
            break
    if(flag == 1):
        return True
    else:
        return False

lst=[]
n = int(input("Enter no of elements : "))
for i in range(0,n):
    a = int(input("Enter element the in list: "))
    lst.append(a)

print(expanding(lst))