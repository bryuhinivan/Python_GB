# Задача № 43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод: 1 2 3 2 3
# Вывод: 2

# list1 = [int(i) for i in input("Введите список целых чисел через пробел: ").split()]
# dict1 = dict()
# dict2 = dict()
# for i in list1:
#     if i not in dict1:
#         dict1.update({i: 1})
#     else:
#         dict1[i] = dict1.get(i) + 1
#     for i in dict1.keys():
#         dict2.update({i: ((dict1.get(i) - 1) * (dict1.get(i))) // 2})
# print(sum(dict2.values()))
# # ((n-1) * n)/2


string = input('Введите элементы списка через пробел -> ').split()
dict = {}
for i in string:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

counter = 0
for key, val in dict.items():
    counter += ((val)*(val-1))//2
print(counter)
