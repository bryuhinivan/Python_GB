# Задача 33. Дано вещественное число, показать сумму его цифр.
# Ввод: 3.12
# Вывод:6
'''
def sumnumber():
    number = 3.1222
    num_str = str(number)
    splited = str(number).replace('.', '')
    result = sum(map(lambda x: int(x), splited)) # result = sum([int(i) for i in splited]) тоже самое
    print(result)
    # print(sum(map(lambda x: int(x), str(number).replace('.', ''))))

sumnumber()
'''
num = float(input())
res = list(filter(lambda x: x != ".", str(num)))
res1 = sum(list(map(int, res)))
print(res1)
