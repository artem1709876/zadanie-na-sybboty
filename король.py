x1 = int(input('введите клетку по оси X: '))
y1 = int(input('введите клетку по оси Y: '))
x2 = int(input('введите клетку по оси X2: '))
y2 = int(input('введите клетку по оси Y2: '))
if x1==x2-1 and y1==y2-1:
    print('YES')
else:
    print('NO')