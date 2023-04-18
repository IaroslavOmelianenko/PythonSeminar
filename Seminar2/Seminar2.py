# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

# number = int(input('Введите предел:'))

# factorial = 1
# i = 1

# while factorial <= number:
#   factorial *= i
#    i += 1

# for i in range (number):
#    factorial *= i

# print(f'Factorial {number} = {factorial}')


# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6
# 0,1,1,2,3,5,8

# nat_number = int(input('Введите натуральное число: '))
#
# i = 0
# temp1 = 0
# temp2 = 1
#
# for i in range (3, nat_number+2):
#     temp = temp2
#     temp2 = temp2 + temp1
#     temp1 = temp
#
#     if nat_number == temp2:
#
#         print(f'По счету число {i}')

'''
Уставшие от необычно теплой зимы, жители решили узнать,действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день.
Температуры – целые числа и лежат в диапазоне от –50 до 50

Input: 6 -> -20 30 -40 50 10 -10
Output: 2
'''

# import random
#
# days = int(input("Введите кол-во дней: "))
# temp_maximum = 0
# temp_new_maximum = 0
#
# for i in range(days):
#     day_temperature = random.randint(-50, 50)
#     print(f"{day_temperature}", end=' ')
#     if day_temperature > 0:
#         temp_new_maximum += 1
#         if temp_new_maximum > temp_maximum:
#             temp_maximum = temp_new_maximum
#     else:
#         temp_new_maximum = 0
#
# print(f'\nСамая длинная оттепель (дней подряд): {temp_maximum}')


'''
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов.
Вторая строка содержит N чисел, записанных на новой строчке каждое.
Здесь каждое число – это масса соответствующего арбуза

Input: 5 -> 5 1 6 5 9
Output: 1 9
'''

import random

watermelon_quantity = int(input('Кол-во арбузов: '))

watermelon_weight = random.randint(1, 10)
min_weight = watermelon_weight
max_weight = watermelon_weight
print(watermelon_weight, end=' ')

for i in range(watermelon_quantity-1):
    watermelon_weight = random.randint(1, 10)
    print(watermelon_weight, end=' ')
    if watermelon_weight > max_weight: max_weight = watermelon_weight
    if watermelon_weight < min_weight: min_weight = watermelon_weight

print(f'\nСамый легкий: {min_weight}, Самый тяжелый арбуз: {max_weight}')
