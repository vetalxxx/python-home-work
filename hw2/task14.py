# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите N: '))
a = 0
count = 0
while a <= n/2:
    a = 2**count
    count += 1
    print(a)
