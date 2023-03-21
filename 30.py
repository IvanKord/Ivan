a = input("введите двухзначное число")
b = len(a)
a = int(a)
if b == 2:
    print(a%10, a//10, sep='')
else: 
    print('число не является двухзначным')
    
