#wap to define a dictionary with employee id as a key and 
#name of an employee as its value. iterate over a dictionary to print these elements.
a = {1: 'veer', 2: 'ishika', 3: 'tanuja', 4: 'vishal'}
key = 0
value = 0
for key,value in a.items():
    a[key] = value
    print("Key: ", key)
    print("value: ", value)
    