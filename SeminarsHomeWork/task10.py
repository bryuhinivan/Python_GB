# Задача 10. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

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