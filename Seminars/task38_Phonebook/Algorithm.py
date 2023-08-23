# Задача № 49. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии

# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм

# 1 - добавление контакта
# 2 - вывод всех контактов
# 3 - поиск по фамилии или имени или отчеству или телефону
# 4 - изменение контакта
# 5 - удаление контакта
# 6 - выход

from Interface import *
from WorkWithFile import *

while True:
    interface()
    command = int(input('Введите команду: '))
    if command == 1:
        person = input('Введите данные пользователя: ')
        add_person(person)
    elif command == 2:
        show_all()
    elif command == 3:
        name = input('Введите элемент для поиска: ')
        search_element(name)
    elif command == 4:
        file_path = 'Phonebook.txt'
        old_name = input('Введите элемент, который хотите заменить: ')
        new_name = input('Введите элемент, на который хотите заменить: ')
        change_data_in_file(file_path, old_name, new_name)
    elif command == 5:
        file_path = 'Phonebook.txt'
        name = input('Введите элемент, который хотите удалить: ')
        delete_data_from_file(file_path, name)
    elif command == 6:
        break
    else:
        print('Ввод некорректен')