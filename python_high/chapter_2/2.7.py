
n = 0
row = 5
while n < row:
    n += 1
    end = row * 2 - 1
    right = row - n
    left = row + n
    l = 1
    while l < row * 2:
        if l > right and l < left:
            print("*", end='')
            # print('%')
        else:
            print(' ', end='')
            # print('$')
        l += 1
    print()


#2
row = 5
for seet in range(row):
    for i in range(row - seet - 1):
        print(' ', end='')
    for j in range(seet * 2 + 1):
        print('*', end='')
    print()


