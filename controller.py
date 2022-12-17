from model import *
from view import *

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    return [last_name, first_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель (';', ',', ':', 'Enter'): ")
    if sep == "":
        sep = None
    return sep

def action_choice():
    print("Здравствуйте!\n\
    Что будем делать:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Данные не обнаружены")