'''
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

Пример:
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

def number_exponentation(number, power):
  if power == 1:
    return number
  else:
    return number*number_exponentation(number, power-1)

my_number = int(input('Введите число:'))
my_power = int(input('Введите степень:'))
print(f'{my_number}^{my_power} = {number_exponentation(my_number,my_power)}')