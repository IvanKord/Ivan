a = int(input("Введите четырёхзначное число: "))
if a > 999 and a < 10000:
    a1 = a // 1000
    a2 = a // 100 % 10
    a3 = a // 10 % 10
    a4 = a % 10
    if a1 + a2 == a3 + a4:
        print("Сумма первых двух цифр равна сумме двух последних чисел", a)
    else:
        print("Сумма первых двух цифр не равна сумме двух последних чисел", a)
    if (a1 + a2 + a3 + a4) % 3 == 0:
        print("Сумма цифр", a, "кратна трем")
    else:
        print("Сумма цифр", a, "не кратна трем")
    if (a1 * a2 * a3 * a4) % 4 == 0:
        print("Произведение цифр", a, "кратно четырем")
    else:
        print("Произведение цифр", a, "не кратно четырем")
    if (a1 * a2 * a3 * a4) % a == 0:
        print("Произведение цифр", a, "кратно числу", а)
    else:
        print("Произведение цифр", a, "не кратно числу", a)
else:
    print('число не является четырёхзначным')