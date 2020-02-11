number = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
l = {'k1':[], 'k2':[]}

for n in number:
    if n < 66:
        l['k2'].append(n)
    else:
        l['k1'].append(n)

print(l)
