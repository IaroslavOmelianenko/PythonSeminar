'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
'''
import random

bushes_quantity = int(input('Введите количество кустов: '))

berries_quantity_on_bushes = [random.randint(1, 10) for i in range(bushes_quantity)]

print(f'Кол-во ягод на кустах: {berries_quantity_on_bushes}')

berries_picking_count = list()
for i in range(bushes_quantity - 1):
    berries_picking_count.append(
        berries_quantity_on_bushes[i - 1]
        + berries_quantity_on_bushes[i]
        + berries_quantity_on_bushes[i + 1]
    )

berries_picking_count.append(
    berries_quantity_on_bushes[-2]
    + berries_quantity_on_bushes[-1]
    + berries_quantity_on_bushes[0]
)

print(f'За раз модуль соберёт максимум {max(berries_picking_count)}')
