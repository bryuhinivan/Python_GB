# Задача 14. Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.

# 10 -> 1 2 4 8

number = int(input('Введите число: '))
i = 0
while 2 ** i <= number:
    print(2 ** i)
    i = i + 1
print('Выше выведены все степени двойки от 0 до i не превосходящие введённого числа number')