# Задача 18. Требуется найти в массиве list_1 самый близкий по величине элемент
# к заданному числу k и вывести его.

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

import sys
list_1 = [1, 2, 3, 4, 5]
k = 6

for i in list_1:
    if i - k == 0:
        print(i)
        sys.exit()

for i in list_1:
    if i - k == -1 or i - k == 1:
        print(i)

















# print(list_1)
# list_1.append(k)
# print(list_1)




















# list_2 = []
# for i in list_1:
#     list_2.append(k - i)
# print(list_2)



