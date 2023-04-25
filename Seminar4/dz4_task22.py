'''
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаютсяв обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
'''

import random

set_size_1 = int(input('Кол-во элементов первого множества:'))
set_size_2 = int(input('Кол-во элементов второго множества:'))

numbers_1 = [random.randint(1, 100) for i in range(set_size_1)]
numbers_2 = [random.randint(1, 100) for i in range(set_size_2)]

print(f'Набор чисел 1: {numbers_1}')
print(f'Набор чисел 2: {numbers_2}')

set_of_numbers_1 = set(numbers_1)
set_of_numbers_2 = set(numbers_2)

result_set = set_of_numbers_1.intersection(set_of_numbers_2)
result_set = sorted(result_set)
print(f'Числа без повторений в порядке возрастания, которые встречаются в обоих наборах:\n{result_set}')
