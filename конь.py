x1 = int(input('введите клетку по оси X: '))
y1 = int(input('введите клетку по оси Y: '))
x2 = int(input('введите клетку по оси X2: '))
y2 = int(input('введите клетку по оси Y2: '))
if abs(x1-x2) == 1 and abs(y1-y2) == 2 or abs(x1-x2) == 2 and abs(y1-y2) == 1:
    print('YES')
else:
    print('NO')