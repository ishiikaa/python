def greatest_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1,"is the greatest number")
    elif num2 > num1 and num2 > num3:
        print(num2, "is the greatest number")
    elif num3 > num1 and num3 > num2:
        print(num3, "is the greatest number")
    else:
        print("invalid input")
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
greatest_num(a, b, c)

