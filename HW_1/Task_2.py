## На вход дается любое квадратичное уравнение, задачей является написание кода, который будет решать это уравнение

# Kвадратного уравнения : ax2+bx+c=0     а!= 0
#
#  Формула квадратного уравнения :
#  x1 = (-b + _/ b2 - 4ac) / 2a         not (D<0)
#  x2 = (-b - _/ b2 - 4ac) / 2a

import math

a = int(input('Введите значение "а": '))
b = int(input('Введите значение "b": '))
c = int(input('Введите значение "c": '))

Descriminant = (b ** 2 - 4 * a * c)
x1 = (-b + math.sqrt(Descriminant))
x2 = (-b - math.sqrt(Descriminant))

print(f' x1 = {x1}')
print(f' x2 = {x2}')






