# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# arr =[]

# while True:
#     n = int(input('Введите длину списка -> '))
#     if n > 0:
#         break

# while n > 0:
#     a = int(input('Введите число -> '))
#     arr.append(a)
#     n -= 1


# while True:
#     k = int(input('Введите длину сдвига k -> '))
#     if k > 0:
#         break


# arr_2 = []

# for i in arr[k:]:
#     arr_2.append(i)
# for i in arr[:k]:
#     arr_2.append(i)

# print(arr_2)

# import random

# array_frs = []

# while True:
#     a = input('Как вы хотите заполнить список. Напишите (вручную или автоматически) -> ')
#     if a == 'вручную' or a == 'автоматически':
#         break

# while True:
#     array_len = int(input('Введите длину списка -> '))
#     if array_len > 0:
#         break

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

# print(array_frs)
# array_scnd = []

# while True:
#     p = input('В какую сторону вы хотите сдвинуть массив (влево/вправо) -> ')
#     if p == 'влево' or p == 'вправо':
#         break

# while True:
#     k = int(input('Введите (k - кол-во на которое нужно сместить) -> '))
#     if k > 0:
#         break

# if p == 'вправо':
#     array_frs = list(reversed(array_frs))
# for i in array_frs[k:]: #[len - k:] - 12 строчек
#     array_scnd.append(i)
# for i in array_frs[:k]: #[:len - k]
#     array_scnd.append(i)
# if p == 'вправо':
#     array_scnd = list(reversed(array_scnd))

# print(array_scnd)

spisok = [1,2,3,4,5,6,7]
k = int(input("Введите значение"))
spisok = spisok[len(spisok) - k :] + spisok[:len(spisok) - k]
print(spisok)