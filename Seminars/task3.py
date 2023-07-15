# 1. В некоторой школе решили набрать три новых математических класса и 
# оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, 
# которое нужно приобрести для них.

# **Input:**
# 20 -- 10
# 21 -- 11
# 22 -- 11
# **Output:**
# 32

firstClass = int(input("Введите количество учеников в 1 классе: "))
secondClass = int(input("Введите количество учеников в 2 классе: "))
thirdClass = int(input("Введите количество учеников в 3 классе: "))

countPartsInClass1 = firstClass // 2 + firstClass % 2
countPartsInClass2 = secondClass // 2 + secondClass % 2
countPartsInClass3 = thirdClass // 2 + thirdClass % 2

print(countPartsInClass1 + countPartsInClass2 + countPartsInClass3)