sub1 = int(input("Enter marks 1: "))
sub2 = int(input("Enter marks 2: "))
sub3 = int(input("Enter marks 3: "))
sum = sub1 + sub2 + sub3

if(sum/3 > 40):
    print("Student passes in all three combined subjects")
else:
    print("Student fails in all three combined subjects")
    
if(sub1<33 or sub2<33 or sub3<33):
    print("student fails")
else:
    print("Student passes")
    

    