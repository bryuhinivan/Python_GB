# Задача 12. Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

sum = int(input('Введите сумму двух чисел: '))
multi = int(input('Введите произведение двух чисел: '))
flag = True

for i in range(sum):
    if multi == (sum - i) * i and flag:
        print(f'Загаданные числа равны: {i} и {sum - i}')
        flag = False


