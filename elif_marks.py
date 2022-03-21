a = int(input("Enter marks"))
b = int(input("Enter marks"))
c = int(input("Enter marks"))
d = int(input("Enter marks"))
e = int(input("Enter marks"))
f = int(input("Enter marks"))
x = a+b+c+d+e+f/6
if x in range(90,100):
    print("Excellent")
elif x in range(80,90):
    print(" A")
elif x in range(70,80):
    print("B")
else:
    print(" Unknown")