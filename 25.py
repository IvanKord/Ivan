a1, b1 = int(input("Введите время (в сек): ")), int(input("Введите скорость (в м/с): "))
a2, b2 = int(input("Введите время (в сек): ")), int(input("Введите скорость (в м/с): "))
if a1 * b1 == a2 * b2:
    print("Расстояния одинаковы")
elif a1 * b1 > a2 * b2:
    print("Первое расстояние больше")
else:
    print("Второе расстояние больше")