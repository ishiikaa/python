#a = input("Enter email address: ")#xyz@gmail.com 1 2 3(check 4)5 6 7 8 9 (checck 10)
#if a[-4] == '.' and a[-10] == '@':
#    print(a)
#else:
#    print("Please enter a valid email address")
email = input("Enter email: ")

if "@" and "." in email:
    print("Valid")
else:
    print("Invalid")