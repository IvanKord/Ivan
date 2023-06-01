def schet():
    a=input("Введите первое число: ")
    a=float(a)
    b=input("Введите второе число: ")
    b=float(b)
    c=input("Введите третье число: ")
    c=float(b)
    if a>b:
        print(a-b)
    elif a>c:
        print(a*c)
    elif a<c:
        print(a**c)
    else:
        print(b-a)
    return a,b,c

b, n, m=schet ()
q, w, e=schet ()
x, y, z=schet ()
