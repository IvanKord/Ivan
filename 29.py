a1, b1 = int(input("Масса первого вещества: ")), int(input("Объем первого вещества: "))
a2, b2 = int(input("Масса второго вещества: ")), int(input("Объем второго вещества: "))
if a1 / b1 == a2 / b2:
    print("Плотности веществ одинаковы")
elif a1 / b1 > a2 / b2:
    print("Плотность первого выщества больше")
else:
    print("Плотность второго выщества больше")
