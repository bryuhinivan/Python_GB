# Задача 2: Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0) 

n = int(input("Введите трёхзначное число: "))

num1 = n // 100
# print(num1)

numtemp = n // 10
num2 = numtemp % 10
# print(num2)

num3 = n % 10
# print(num3)

res = num1 + num2 + num3
print(res) 