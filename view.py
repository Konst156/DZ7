def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
        print("-"*85)
        for i in data:
            print(i[0].center(20), i[1].center(20), i[2].center(15), i[3].center(30))
    else:
        print("Справочник пуст!")  