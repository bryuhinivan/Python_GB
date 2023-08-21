# Задача. Дан список целых чисел, оставить в нём только двузначные числа
'''
list_1 = [1, -13, 45, -2, -100, 664, 56]
new_array = list(filter(lambda x: 10 <= abs(x) <= 99, list_1)) # функция abs вычисление по модулю
print(new_array)
'''


arr = map(int,input('Введите число: ').split())
arr_res = list(filter(lambda x: x in range(10,100), arr))
print(arr_res)
