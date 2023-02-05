# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2
# *
import random
number_eagles = 0
number_tails = 0
num = int(input('Введите число монет: '))
my_list = []
for _ in range(num):
    my_list.append(random.randint(0, 1))
print(num, ' -> ', my_list)

for i in range(len(my_list)):
    if my_list[i] == 0:
        number_eagles += 1
    elif my_list[i] == 1:
        number_tails += 1
if number_eagles > number_tails:
    print(number_tails)
elif number_tails > number_eagles:
    print(number_eagles)
else:
    print(number_eagles)
