def thert():
    a = input("Введите трёхзначное число - ")
    try:
        a = int(a)
        if 99 < a < 1000:
            a1 = a // 100
            a2 = a % 10 //10
            a3 = a % 10
            print("Разница - " ,(a - ( a3*100 + a2*10 + a1)) )
        else:
            print("Число должно быть трёхзначным")
    except ValueError:
        print("Допускаются только цифры")
thert()
