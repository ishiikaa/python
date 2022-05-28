pos = 0
neg = 0
zero = 0
for i in range(1,11):
    a = int(input(f'Enter no{i}: '))
    if a<0:
        neg+=1
        
    elif a == 0:
        zero+=1
        
    elif a>0:
        pos+=1
print("Negative number: ",neg) 
print("Positive number: ",pos)
print("Zero number: ",zero)