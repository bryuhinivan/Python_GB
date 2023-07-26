# Задача 10. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# import random # Модуль random позволяет генерировать случайные числа.
                # Прежде чем использовать модуль, необходимо подключить его с помощью инструкции import random
# import math   # Этот модуль предоставляет обширный функционал для проведения вычислений
                # с вещественными числами (числами с плавающей точкой)

# while True:
#     num = int(input('Введите количество монет на столе: '))
#     if num == 0:
#         print(0)
#         break
#     if num > 0:
#         break

# coins_array = []
# count_one = 0
# count_zero = 0

# while num > 0:
#     coins_array.append(random.randint(0, 1))
#     num = num - 1
# print(coins_array)

# for i in range(0,len(coins_array)):
#     if coins_array[i] == 0:
#         count_zero = count_zero + 1
#     else:
#         count_one = count_one + 1

# if count_one > count_zero:
#     print(f'Минимальное количество монет, которое'
#           f' надо перевернуть - {count_zero}')
# else:
#     print(f'Минимальное количество монет, которое'
#           f' надо перевернуть - {count_one}')

import random 

while True:
    number_coins = int(input('Введите количество монет на столе: '))
    if number_coins == 0:
        print(0)
        break
    if number_coins > 0:
        break

coints_array = []
coint_side = 0
coint_back_side = 0

while number_coins > 0:
    coints_array.append(random.randint(0, 1))
    number_coins = number_coins - 1
print(coints_array)

for i in range(0, len(coints_array)):
    if coints_array[i] == 0:
        coint_side = coint_side + 1
    else:
        coint_back_side = coint_back_side + 1

if coint_side > coint_back_side:
    print(f'Минимальное количество монет, которое надо перевернуть - {coint_back_side}')
else:
    print(f'Минимальное количество монет, которое надо перевернуть - {coint_side}')