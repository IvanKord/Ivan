def thert():
    a = int(input("Введите число - "))
    stack = []
    try:
        while a > 0:
            stack.append(a % 10)
            a //=10
        while stack:
            print(stack.pop(), end=' ')
    except ValueError:
        print("Допускаются только цифры")
thert()
