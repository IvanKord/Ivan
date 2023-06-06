def bank():
    yeas = input("На сколько лет хотите сделать вклад?    ")
    a = input("Какая сумма вклада?    ")
    try:
        yeas = int(yeas)
        a = int(a)
        b = a*1.1**yeas
        return print("Ваша сумма будет равна - " , b)
    except ValueError:
        print("Допускаются только цифры")
bank()
