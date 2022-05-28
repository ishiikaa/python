n = int(input("Enter no. of employees: "))
for i in range(0,n):
    j_no = int(input("Enter job no. : "))
    l_no = int(input("Enter level no. : "))
    b_pay = int(input("Enter basic pay : "))

    rent = b_pay * (25 / 100)
    tax = 0

    if  l_no == 1:
        gross = b_pay + rent + 1500
    elif l_no == 2:
        gross = b_pay + rent + 950
    elif l_no == 3:
        gross = b_pay + rent + 600
    elif l_no == 4:
            gross = b_pay + rent + 250
    else:
        print("wrong input")

    if gross <= 2000:
        print("No tax deduction")
    elif gross > 2000 and gross <= 4000:
        tax = gross * (3/100) 
    elif gross > 4000 and gross <= 5000:
        tax = gross * (5/100)
    elif gross > 5000:
        tax = gross * (8/100)
    print("Job no.: ", j_no)
    print("level no.: ", l_no)
    print("basic pay: ", b_pay)
    print("tax = ",tax, 'rs')
    net_sal = gross - tax 
    print ('net salary is: ', net_sal)