'''
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:3 4 2 5 7
[4,6]
Вывод:1, 3
'''



array = []
count = int(input("Введите количество элементов в списке: "))
for i in range(0, count):
    element = int(input("Введите элемент в список: "))
    array.append(element)
print(array)

num1 = int(input("Введите min-ое число в списке: "))
num2 = int(input("Введите max-ое число в списке: "))

for i in range(0, len(array)):
    res = []
    if array[i] >= num1 and array[i] <= num2:
        res.append(i)
        print(*res, end = " ")
