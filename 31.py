x1, y1, x2, y2, x3, y3 = int(input('введите координаты первой вершины x1=_, y1=_')), int(input('')), int(input('введите координаты второй вершины x2=_, y2=_')), int(input('')), int(input('введите координаты третьей вершины x3=_, y3=_')), int(input()),
print('S=', (1 / 2) * ((((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) ** 2) ** (1 / 2)), 'P=', (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)) + ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** (1 / 2) + ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** (1 / 2) / 2, '')
