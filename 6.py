a = int(input("Введите 5ти значное число:"))
if a < 10000 or a > 99999:
print("плохое число")
else:
a1 = a // 10000
a5 = a % 10
print(a1, a5)