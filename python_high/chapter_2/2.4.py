n = 0
quit = 'a'

while n < 3:
    username = input('username：')
    password = input('password：')
    if username == 'Albert' and password == '1':
        print('hello' + username)
        while quit != 'q':
            quit = input("input 'q' quit the program:")
        break
    else:
        print('password or username wrong')
    n += 1