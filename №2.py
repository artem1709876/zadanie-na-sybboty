try:
    n = input('Введите число: ')
    n = float(n)
except ValueError:
    print("Вы что-то попутали с вводом")
    3 / 0
except ZeroDivisionError:
    print("Деление на ноль")
else:
    print("Все нормально. Вы ввели число", n)
finally:
    print("Конец программы")
