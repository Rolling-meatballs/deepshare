msg_dic = {
    'apple': 10,
    'tesla': 1000000,
    'mac': 10000,
    'iphone': 8000,
    'chicken': 30,
    'pen': 3,
    'ruler': 5
}


def answer():
    print('information of goods:')
    print(msg_dic)
    goods = []
    for k, v in msg_dic.items():
        goods.append(k)
    n = 'continue'
    menu = {}

    while n != 'q':
        name = input("name:")
        number = input("num:")
        if name not in goods:
            print(name, "is sell out, please change one")
            continue
        elif number.isdigit():
            number = int(number)
            menu[name] = number, msg_dic[name]
        else:
            print("please give a right quantity, please try again")
            continue
        print('goods list:', menu)
        n = input("you can input 'q', when you want to quit, if not push ENTER:")

def give_answer():
    goods_list = []
    while True:
        for product, price in msg_dic.items():
            print('product: %s, price: %s' % (product, price))
        choice = input('please choose product>>:').strip()
        if choice == 'q': #user can quit the program by inputting 'q'
            break
        elif choice not in msg_dic:
            print('The product you choose is invalid')
            continue
        else:
            while True:
                count = input('please input the number of the product>>').strip()
                if not count.isdigit():
                    print('The content you input is not number')
                    continue
                else:
                    goods_list.append((choice, msg_dic[choice], count))
                    print(goods_list)
                    break



def main():
    # answer()
    give_answer()


if __name__ == '__main__':
    main()
