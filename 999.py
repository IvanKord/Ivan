## стр. 51
## 1.
x = int(input("Введите значение x - "))
print("y = ", 7 * x + 5)
## 2. 
x = int(input("Введите значение стороны квадрата - "))
print("P = ", x * 4)
## 3.
x = int(input("Введите значение радиуса окружности - "))
print("L = ", x * 2 * 3.14)
## 4.
x = int(input("Введите значение диаметра окружности - "))
print("S = ", x * 2 / 4 * 3.14)
## 5.
from math import *
a = int(input("Введите значение 1 катета - "))
b = int(input("Введите значение 2 катета - "))
print("С = ", sqrt(a**2 + b**2))
## 6.
from math import *
a = int(input("Введите значение 1 катета - "))
b = int(input("Введите значение 2 катета - "))
c = sqrt(a**2 + b**2)
print("P = ", a + b + c)
## 7.
from math import *
a = int(input("Введите значение 1 стороны - "))
b = int(input("Введите значение 2 стороны - "))
print("P = ", 2 * (a + b), "d = ", sqrt(a * 2 + b * 2))
## 8.
a = int(input("Введите R - "))
b = int(input("Введите r - "))
print("S = ", 3.14 * (a**2 - b**2))
## 9.
a = int(input("Введите ребро куба - "))
print("S = ", 6 * a**2, "V = ", a**3)
## 10.
from math import *
a = int(input("Введите значение меньшего основания - "))
b = int(input("Введите значение большего основания - "))
h = int(input("Введите значение высоты - "))
c = sqrt(a**2 + b**2)
print("P = ", a + b + c + с)
## 11.
a = int(input("Введите значение массы - "))
b = int(input("Введите значение объема - "))
print("p = ", a / b)
## 12. 
a = int(input("Введите значение 1 числа - "))
b = int(input("Введите значение 2 числа - "))
print(a, "+", b, "=", a+ + b, ", ", a, "-", b, "=", a - b, ", ", a, "*", b, "=", a * b, ", ", a, ":", b, "=", a / b)
## 13.
from scipy. stats import gmean
a = int(input("Введите значение 1 числа - "))
b = int(input("Введите значение 2 числа - "))
if a > 0 and b > 0:
    print((a + b) / 2, ", ", gmean([a, b]))
else:
    print("одно из чисел отрицательное")
## 14. 
a = int(input("Введите значение количества населеления - "))
b = int(input("Введите значение плошади населения - "))
print("Плотность населения -", a / (b**2))
## 15.
a = int(input("Введите значение ребра параллепипеда - "))
b = int(input("Введите значение ребра параллепипеда - "))
c = int(input("Введите значение ребра параллепипеда - "))
print("S =", 2 * (a * b + a * c + b * c), "V =", a * b * c)

## стр. 52-53
## 1.
a = int(input("Введите значение 1 числа - "))
b = int(input("Введите значение 2 числа - "))
if a != b:
    if a > b:
        print("max =", a, "min =", b)
    else:
        print("max =", b, "min =", a)
else:
    print(b, "=", a)
## 2. 
a = int(input("Введите значение r круга - "))
b = int(input("Введите значение сторону квадрата - "))
if a * 2 > b:
    print("не впишется")
else:
    print("впишется")
## 4.
from math import *
a = int(input("Введите значение r круга - "))
b = int(input("Введите значение сторону квадрата - "))
if a * 2 < sqrt(2 * b):
    print("не впишется")
else:
    print("впишется")

## 5. 
a = int(input("Введите значение 1 числа - "))
b = int(input("Введите значение 2 числа - "))
if a != b:
    if a > b:
        print(a, ">", b)
    else:
        print(b, ">", a)
else:
    print(b, "=", a)
## 7.
a = int(input("Введите значение 1 числа - "))
b = int(input("Введите значение 2 числа - "))
if a != b:
    if a > b:
        print(a, ">", b)
    else:
        print(b, ">", a)
else:
    print(b, "=", a)
## 8.
a = int(input("Введите значение расстояния (km) - "))
b = int(input("Введите значение расстояния (фут) - "))
a = a * 3280.84
if a != b:
    if a > b:
        print(a / 3280.84, ">", b)
    else:
        print(b, ">", a / 3280.84)
else:
    print(b, "=", a / 3280.84)
## 10.
a = int(input("Введите значение 1 числа - "))
b = int(input("Введите значение 2 числа - "))
if a != b:
    if a > b:
        print(a / b)
    else:
        print(b / a)
else:
    print(b / a)
## 11.
a = int(input("Введите значение расстояния (m/s) - "))
b = int(input("Введите значение расстояния (km/h) - "))
a = a * 3.6
if a != b:
    if a > b:
        print(a / 3.6, ">", b)
    else:
        print(b, ">", a / 3.6)
else:
    print(b, "=", a / 3.6)
## 12.
a = int(input("Введите значение r круга - "))
b = int(input("Введите значение сторону квадрата - "))
Sr = 2 * 3.14 * a
Sk = b ** 2
if Sr != Sk:
    if Sr > Sk:
        print("Площадь круга больше площади квадрата")
    else:
        print("Площадь квадрата больше площади круга")
else:
    print("Площади равны")
## 14. 
a = int(input("Введите значение расстояния (дюйм) - "))
b = int(input("Введите значение расстояния (мм) - "))
a = a * 25.4
if a != b:
    if a > b:
        print(a / 25.4, ">", b)
    else:
        print(b, ">", a / 25.4)
else:
    print(b, "=", a / 25.4)
## 15.
a1 = int(input("Введите значение массы (1)- "))
b1 = int(input("Введите значение объема (1)- "))
a2 = int(input("Введите значение массы (2)- "))
b2 = int(input("Введите значение объема (2)- "))
p1 = a1 / b1
p2 = a2 / b2
if p1 != p2:
    if p1 > p2:
        print("(1) > (2)")
    else:
        print("(2) > (1)")
else:
    print("(1) = (2)")
## стр. 53-54
## 1.
i = 10
while i < 23:
    print(i, "=", i * 2.54, "см")
    i += 1
## 2.
a = int(input("курс доллара к рублю - "))
i = 1
while i < 21:
    print(i, "usd =", i * a, "руб.")
    i += 1
## 3. 
a = int(input("e - "))
i = 1
while i < 21:
    print(a ** i)
    i += 1
## 4.
i = 1
while i < 22:
    print(i + 0.1)
    i += 1
## 5.
list=(2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9)
for i in list:
    print(i)
## 6. 
for i in range(2, 41, 2):
    print(i)
## 7.
for i in range(1, 16, 2):
    print(i)
## 8.
from math import *
for i in range(2, 21, 2):
    print(sqrt(i))
## 9.
a = int(input("стоимость 1 кг конфет - "))
for i in range(2, 11, 2):
    print(i * a)
## 10.
def thert():
    a = int(input("a - "))
    b = int(input("b - "))
    n = 100
    x = a
    dx = (b - a) / n
    while x <= b:
        print("x=", x," sqrt(x)=", x ** 0.5)
        x += dx
thert()
## 11.
def thert():
    a = int(input("a - "))
    b = int(input("b - "))
    n = 100
    x = a
    dx = (b - a) / n
    while x <= b:
        print("x=", x," e**x-1=", 2,71 ** x - 1)
        x += dx
thert()
## 14.
for i in range(1, 21, 1):
    t = 1 + i
    print("y=", 2 * (t ** 2) + 2 * t + 2)
## 15.
for i in range(2, 21, 2):
    f = 2 * i
    print("z=", 8 * (f ** 3) - f)













