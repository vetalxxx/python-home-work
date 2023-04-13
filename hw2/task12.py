# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input('Введи чему равна сумма двух натуральных чисел: '))
p = int(input('Введи чему равно произведение двух натуральных чисел: '))
d = s*s - 4*p
if d >= 0:
    x = (s + d**0.5)/2
    y = (s - d**0.5)/2
    if int(x) == float(x) and int(y) == float(y):
        print(f'искомые числа {int(x)} и {int(y)}')
    else:
        print(f'таких чисел не найти')
else:
    print(f'таких чисел не найти')
