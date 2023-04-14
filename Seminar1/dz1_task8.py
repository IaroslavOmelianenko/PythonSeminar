'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

Пример:
3 2 4 -> yes
3 2 1 -> no
'''

print('Your chocolate bar size is m*n')
n_size = int(input('Enter n size of chocolate bar:'))
m_size = int(input('Enter m size of chocolate bar:'))
k_pieces = int(input('Enter how many pieces you want:'))
print(f'Your chocolate bar is {n_size}*{m_size} pieces. Can we split your chocolate bar?')

if k_pieces%n_size != 0 and k_pieces%m_size != 0:  print ('No')
else: print ('Yes')