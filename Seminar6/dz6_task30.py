'''
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

number = int(input('Введите число: '))
step = int(input('Введите шаг: '))
elements_quantity = int(input('Введите кол-во элементов: '))

numbers_array = [None] * elements_quantity

for i in range(elements_quantity):
    numbers_array[i] = number + i * step

print(numbers_array)