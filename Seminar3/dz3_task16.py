'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

Пример:
5
1 2 3 4 5
3
-> 1
'''

import random

number_of_elements = int(input('Ввдеите количество элементов в массиве:'))
my_list = [random.randint(1, 10) for i in range(number_of_elements)]
print(my_list)

my_number = int(input('Ввдеите число, которое будем искать в массиве:'))
counter = 0
for i in my_list:
    if i == my_number: counter += 1

print(f'Число "{my_number}" повторяется в списке {counter} раз(а)')