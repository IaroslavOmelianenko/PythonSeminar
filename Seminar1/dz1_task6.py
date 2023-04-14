'''
Задача 6: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

Пример:
385916 -> yes
123456 -> no
'''


ticket_number = input('Is your ticket lucky? Enter your ticket number:')
if (len(ticket_number) != 6):
    print ('Ticket number cant contain more or less than 6 digits. Try again.')
else:
  if int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2]) == int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5]):
    print ('Yes')
  else: print ('No')