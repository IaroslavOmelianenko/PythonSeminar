'''
Задача 2: Найдите сумму цифр трехзначного числа.

Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

number = int(input('Enter number with 3 digits:'))
if (number < 100) or (number > 999):
    print ('Number contains more or less than 3 digits. Try again.')
else:
  digit_1 = number%1000 // 100
  digit_2 = number%100 // 10
  digit_3 = number%10
  print(f'Sum of digits from number {number} is {digit_1+digit_2+digit_3} ({digit_1}+{digit_2}+{digit_3})')