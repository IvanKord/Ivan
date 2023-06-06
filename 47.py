def thert():
    a = int(input("Введите число - "))
    try:
        if '2' in str(a):
            print("Цифра 2 входит в число ", a)
        else:
            print("Цифра 2 не входит в число ", a)
    except ValueError:
        print("Допускаются только цифры")
thert()
