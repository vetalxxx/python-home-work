# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 3 -> 1

n = int(input('Введите количество элементов массива: '))
my_array = [int(input(f'Введите {i+1} элемент массива: ')) for i in range(n)]
print(my_array)
x = int(input('Какую цифру ищем?: '))
count = 0
for i in range(0, len(my_array)):
    if my_array[i] == x:
      count +=1
print(f'{x} встречается -> {count} раз')