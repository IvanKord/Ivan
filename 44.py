def thert():
    a = input("Введите пятизначное число - ")
    try:
        a = int(a)
        if 9999 < a < 100000:
            a1 = a%10
            a4 = a%100//10
            print("Предпоследняя - ", a4 , "Последняя - ", a1)
        else:
            print("Число должно быть пятизначным")
    except ValueError:
        print("Допускаются только цифры")
thert()
