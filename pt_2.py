a = int(input("Enter no. of elements: "))
list1 = []
for i in range(0,a):
    c = int(input('Enter elements: '))
    list1.append(c)
dict1 = {}
for i in list1:
    dict1[i] = i**3 
key = 0
value = 0
for key, value in dict1.items():
    dict1[key] = value
    print("key: ", key, "value: ", value)