# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет: '))
countEagle = 0
countTails = 0
for i in range(n):
    x = input(f"{i+1}-ая монета Орел или решка?: ").lower()
    if x == 'орел':
        countEagle += 1
    else:
        countTails += 1
if countEagle > countTails:
    print(f"Перевернуть нужно {countTails} монет, те что лежат решкой вверх")
else:
    print(f"Перевернуть нужно {countEagle} монет, те что лежат орлом вверх")
