'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''

import random

number_of_elements = 10
my_list = [random.randint(-10, 10) for i in range(number_of_elements)]
print(my_list)

min_value = int(input('Введите минимум: '))
max_value = int(input('Введите максимум: '))

list_of_indexes = []
for i in range(len(my_list)):
    if min_value <= my_list[i] <= max_value:
        list_of_indexes.append(i)

print(f'Индексы чисел от {min_value} до {max_value}: {list_of_indexes}')

