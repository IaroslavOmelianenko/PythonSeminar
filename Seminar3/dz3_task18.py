'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

Пример:
5
1 2 3 4 5
6
-> 5
'''

import random

number_of_elements = int(input('Ввдеите количество элементов в массиве:'))
my_list = [random.randint(0, 100) for i in range(number_of_elements)]
print(my_list)

my_number = int(input('Ввдеите число (0-100), близкое к которому будем искать в массиве:'))
the_nearest_number = my_list[0]
for i in my_list:
    if abs(i - my_number) < abs(the_nearest_number - my_number):
        the_nearest_number = i

print(f'Число {the_nearest_number} самое близкое к числу {my_number}')