from math import *
a, b = int(input("Введите радиус круга: ")), int(input("Введите сторону квадрата: "))
if a ** 2 * pi == b ** 2:
    print("Площади равны")
elif a ** 2 * pi > b ** 2:
    print("Площадь круга больше")
