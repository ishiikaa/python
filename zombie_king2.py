a = ['abc', 'xyz', 'aba', '1221']
b = []
for i in a:
    if a[i][0] == a[i][-1] and len(i) > 2:
        b.append(i)
print(b)