cord_cl1_X = int(input('введите клетку по оси X: '))
cord_cl1_Y = int(input('введите клетку по оси Y: '))

cord_cl2_X = int(input('введите клетку по оси X: '))
cord_cl2_Y = int(input('введите клетку по оси Y: '))

if (cord_cl2_Y + cord_cl1_Y + cord_cl2_X + cord_cl1_X) %2 ==0 :
    print('YES')
else:
    print('NO')