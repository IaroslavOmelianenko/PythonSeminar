'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
'''

def sum(number_1, number_2):
  if number_2 == 0:
    return number_1
  else:
    return sum(number_1 + 1, number_2 - 1)

my_number_1 = int(input('Введите первое число:'))
my_number_2 = int(input('Введите второе число:'))
print(f'Сумма: {sum(my_number_1,my_number_2)}')