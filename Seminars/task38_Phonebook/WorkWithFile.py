def add_person(person):
    data = open('Phonebook.txt', 'a', encoding='utf-8')
    data.write(person)
    data.write('\n')
    print('Данные успешно добавлены в список контактов.')
    data.close()

def show_all():
    print('Список контактов: ')
    data = open('Phonebook.txt', 'r', encoding='utf-8')
    for line in data:
        print(line[:-1])
    data.close()

def search_element(name):
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if name in line.split():
                print(line)
                break
        else:
            print('Такого нет.')

def change_data_in_file(file_path, old_name, new_name):
    with open(file_path, 'r+', encoding='utf-8') as data:
        lines = data.readlines()
        data.seek(0)  # перемещаем курсор в начало файла
        for line in lines:
            if old_name in line:
                line = line.replace(old_name, new_name)
            data.write(line)
        data.truncate()  # усекаем оставшуюся часть файла, если новый текст короче предыдущего 
        print('Данные успешно изменены.')                     

def delete_data_from_file(file_path, name):
    with open(file_path, 'r', encoding='utf-8') as data:
        lines = data.readlines()
    with open(file_path, 'w', encoding='utf-8') as data:
        for line in lines:
            # Проверяем, содержит ли текущая строка данные, которые нужно удалить
            if name not in line:
                data.write(line)
        print('Данные успешно удалены из файла.')
    
