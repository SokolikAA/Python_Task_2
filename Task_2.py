# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *

summa = int(input('Введите сумму загаданых чисел: '))
product = int(input('Введите произведение загаданых чисел: '))
first_number = 1
second_number = 1
for first_number in range(1, 1000):
    for second_number in range(1, 1000):
        if first_number + second_number == summa and first_number * second_number == product:
            print(f'{summa} {product} -> {first_number} {second_number}')
