def balans():
    purchase = {}
    while True:
        print('1. пополнение счета ')
        print('2. покупка ')
        print('3. история покупок ')
        print('4. выход ')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            cash = int(input('Введите сумму на сколько пополнить счет :'))
            cash += cash
            continue
        elif choice == '2':
            buy = int(input('Введите сумму покупки :'))
            if cash > buy:   #если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
                cash -= buy
                product = input('Введите название покупки :')
                purchase[product] = buy
        elif choice == '3':
            print(purchase)

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

