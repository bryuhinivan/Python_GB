# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах

list_number = [1, 10, 2, 3, 7, 9, 12, 0, 5, 7, 8]
max_num = list_number[0]
for el in list_number:
    if el == 0:
        print(max_num)
        break
    elif el > max_num:
        max_num = el

# list = [1, 4, 3, 0]
# max = list[0]
# index = 0
# while list[index] != 0:
#         if list[index] > max:
#             max = list[index]
#         index += 1    
# print(max)