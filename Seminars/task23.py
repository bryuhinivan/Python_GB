# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

array = [0, -1, 5, 2, 3]
print(len([array[i] for i in range(1, len(array)) if array[i-1] < array[i]]))


# import random
#
# array_frs = []
#
# while True:
#     a = input('Как вы хотите заполнить список. Напишите (вручную или автоматически) -> ')
#     if a == 'вручную' or a == 'автоматически':
#         break
#
# while True:
#     array_len = int(input('Введите длину списка -> '))
#     if array_len > 0:
#         break
#
# # Заполнение списка
# if a == 'вручную':
#     i = 1
#     while i <= array_len:
#         a = int(input(f'Введите {i} элемент списка -> '))
#         array_frs.append(a)
#         i += 1
# if a == 'автоматически':
#     while array_len > 0:
#         a = random.randint(-20, 20)
#         array_frs.append(a)
#         array_len -= 1
#
# print(array_frs)
# count = 0
# res_array = ''
#
#
# for i in range(1, len(array_frs)):
#     frst, scnd = array_frs[i-1], array_frs[i]
#     if frst < scnd:
#         res_array += ' (' + str(frst) + ' < ' + str(scnd) + ') '
#         count += 1
#
#
# print(f'Количество элементов которые больше предыдущих -  {count}')
# print(res_array)