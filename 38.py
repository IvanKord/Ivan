def schet():
    a=int(input("Введите первое число в миллиметрах: "))
    b=int(input("Введите второе число а дюймах: "))
    if (a*25.4) > b: 
        print("Первое число длинее")
    else:
        print("Второе число длинее")
    return a,b

c, d=schet()

def schet():
    a1=input("Введите первое число: ")
    a1=float(a1)
    b1=input("Введите второе число: ")
    b1=float(b1)
    if a1>b1:
        print(a1*b1)
    elif a1<b1:
        print(b1**a1)
    return a1,b1

x, y=schet()
