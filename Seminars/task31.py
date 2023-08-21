# Задача 31. Дан список, вывести в отдельном списке буквы, а в другом цифры, используя фильтр.
# ["asd", 1, 2, "gfd"]
# ["asd", "gfd"][1,2]

'''
def res():
    list1 = ['a', 'b', 'c', 1, 2, 3]
    list2 = list(filter(lambda x: type(x) == str, list1))
    print(list2)
    list3 = list(filter(lambda x: type(x) == int, list1))
    print(list3)
res()
'''
arr_in = input('Введите строку -> ').split()
arr_1 = list(filter(lambda x: x.isdigit(), arr_in))
arr_2 = list(filter(lambda x: x.isalpha(), arr_in))
print(arr_1, arr_2) 




