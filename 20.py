x = int(input("Введите х: "))
if x > 0:
    print(f"y=x² y={x ** 2}")
elif x == 0:
    print("x не может быть равен 0")
else:
    print(f"y=1/x² y={1 / x ** 2}")
