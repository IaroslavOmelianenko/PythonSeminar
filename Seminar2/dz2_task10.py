'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
'''
import random

coins_quantity = int(input('Введите кол-во монеток: '))
coin_side = 0
orel_counter = 0
reshka_counter = 0
for i in range(coins_quantity):
    coin_side = random.randint(0, 1)
    ## 0-reshka, 1-orel
    if coin_side == 0:
        reshka_counter += 1
        print('(Решка)')
    else:
        orel_counter += 1
        print('(Орёл)')

print(f'Минимальное количество монет, которые нужно перевернуть: {reshka_counter if orel_counter > reshka_counter else orel_counter}')

