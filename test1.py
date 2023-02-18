a=input()
b=input()
if a=='красный' and b=='красный':
    print('красный')
elif a=='красный' and b=='синий':
    print('фиолетовый')
elif a=='красный' and b=='желтый':
        print('оранжевый')
elif a=='синий' and b=='синий':
    print('синий')
elif a=='синий' and b=='красный':
    print('фиолетовый')
elif a=='синий' and b=='желтый':
        print('зеленый')
elif a=='желтый' and b=='желтый':
    print('желтый')
elif a=='желтый' and b=='синий':
    print('зеленый')
elif a=='желтый' and b=='красный':
        print('оранжевый')
else:
    print('ошибка цвета')