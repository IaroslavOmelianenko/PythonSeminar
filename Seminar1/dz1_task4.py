'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

Пример:
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
'''

cranes_quantity = int(input('Enter paper cranes quantity (multiple of 6):'))
if cranes_quantity%6 !=0:
  print('Children always make cranes a multiple of 6. Try to input crains quantity again.')
else:
  petya_cranes = cranes_quantity // 3 // 2
  katya_cranes = cranes_quantity // 3 * 2
  serega_cranes = petya_cranes
  print(f'Petya made {petya_cranes}, Katya made {katya_cranes}, Serega made {serega_cranes}')