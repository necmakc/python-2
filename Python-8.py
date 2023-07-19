# Задача 1: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
def load_data(data_dict):
    data_dict.clear()
    with open(path, 'r', encoding='utf-8') as data_contacts:
        for item in data_contacts.readlines():
            key, val = item.strip().split(':')
            data_dict[key] = val
    return data_dict


def show_contacts():
    print('\n     -------Список контактов-------')
    k = 1
    for i in data_dict:
        print(f"{k}. {i} {data_dict[i]}")
        k += 1


def add_contact():
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")
    data_dict[name] = number
    print("Контакт успешно добавлен!")


def save_to_file(data_dict):
    with open(path, 'w', encoding='utf-8') as data_contacts:
        for i in data_dict:
            data_contacts.write(i+":"+data_dict[i]+"\n")
    print("Сохранение выполнено!")


def find_contact():
    fl = False
    name = input("Введите критерий для поиска: ")
    for i in data_dict.keys():
        if name.upper() in i.upper():
            print(i, data_dict[i])
            fl = True
    if fl == False:
        print("Контакт не найден!")


def delete_contact():
    temp_dict = dict()
    temp_dict.clear()
    fl = False
    name = input("Введите критерий для поиска: ")
    for i in data_dict.keys():
        if name.upper() in i.upper():
            temp_dict[i] = data_dict[i]
            print(i)
            fl = True
    if fl == False:
        print("Контакт не найден!")
    else:
        answer_delete = input("Удалить найденные контакты?(y/n): ")
        if answer_delete == 'y':
            for i in temp_dict.keys():
                del data_dict[i]


def change_contact(data_dict):
    temp_dict = dict()
    temp_dict.clear()
    fl = False
    k = 1
    name = input("Введите критерий для поиска: ")
    for i in data_dict.keys():
        if name.upper() in i.upper():
            temp_dict[i] = [data_dict[i], k]
            print(k, i)
            k += 1
            fl = True
    if fl == False:
        print("Контакт не найден!")
    else:
        index_contact = input(
            "Введите индекс контакта который хотите изменить: ")
        answer_change = input(
            "Введите 1 если хотите изменить имя контакта или 2 если номер телефона: ")
        if answer_change == '1':
            new_name = input("Введите новое имя контакта: ")
            for k, v in temp_dict.items():
                if str(index_contact) == str(temp_dict[k][1]):
                    del data_dict[k]
                    data_dict[new_name] = temp_dict[k][0]
                    print("Имя контакта изменено!")
        if answer_change == '2':
            new_phone = input("Введите номер телефона: ")
            for k, v in temp_dict.items():
                if str(index_contact) == str(temp_dict[k][1]):
                    data_dict[k] = new_phone
                    print("Номер телефона изменен!")
    return (data_dict)


path = 'phone_book.txt'
data_dict = dict()
load_data(data_dict)

flag = True
while flag:
    print('''\n     -------Меню-------
    0 - Изменить контакт
    1 - Добавить контакт
    2 - Удалить контакт
    3 - Найти контакт
    4 - Показать контакты
    5 - Сохранить в файл
    6 - Загрузить из файла
    7 - Выход''')
    answer = input('\nВведите действие которое хотите выполнить: ')
    if answer == '0':
        change_contact(data_dict)
    if answer == '1':
        add_contact()
    if answer == '2':
        delete_contact()
    if answer == '3':
        find_contact()
    if answer == '4':
        show_contacts()
    if answer == '5':
        save_to_file(data_dict)
    if answer == '6':
        answer_load = input(
            "Несохраненные данные будут потеряны! Продолжить загрузку?(y/n): ")
        if answer_load == 'y':
            print("Загрузка выполнена!")
            load_data(data_dict)
        else:
            print("Загрузка не выполнена!")
    if answer == '7':
        print('Удачи!')
        flag = False
