a = input("Enter item in list: ")
b = input("Enter item in list: ")
c = input("Enter item in list: ")
d = input("Enter item in list: ")
x = [a, b, c, d]
h = input("Enter item you want to find: ")
if (h in x):
    print(h," is in the list")
else:
    print(h," is not in the list")