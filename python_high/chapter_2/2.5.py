n = 0
answer = 'a'

while True:
    if n == 3:
        while True:
            answer = input("input 'Y' or 'y' continue, 'N' or 'n' quit the game:")
            if answer == 'Y' or answer == 'y':
                n = 0
                answer = 'a'
                print('end Y')
                break
            elif answer == 'N' or answer == 'n':
                n = 4
                print('end n')
                break
    elif n < 3:
        age = input('give a age：')
        if age == '27':
            print('congratulation, You WIN')
            break
        else:
            print('try again')
            n += 1
    else:
        break
