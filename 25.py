a, b = int(input("Введите скорость (в км/ч): ")), int(input("Введите скорость (в м/с): "))
if a == b * 3.6:
    print("Скорости равны")
elif a > b * 3.6:
    print(a, 'км/ч больше, чем', b, "м/с")
else:
    print(a, 'км/ч меньше, чем', b, "м/с")
