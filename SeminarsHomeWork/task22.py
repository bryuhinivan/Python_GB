# Задача 22. Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# пример
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите кол-во элементов 1-го списка: "))
m = int(input("Введите кол-во элементов 2-го списка: "))
list_n = []
list_m = []

for i in range(n):
    list_n.append(int(input("Введите значения в список list_n: ")))
print(list_n)
for j in range(m):
    list_m.append(int(input("Введите значения в список list_m: ")))
print(list_m)
list_nm = sorted((set(list_n).intersection(list_m)))
print(list_nm)