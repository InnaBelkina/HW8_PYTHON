# Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. 
# Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание

# Корректность и уникальность данных не обязательны.

# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.

# 2) CRUD: Create, Read, Update, Delete

# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. 
# Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv

# 4) импорт данных из текстового файла формата csv

# Используйте функции для реализации значимых действий в программе

# (*) Усложнение.

# Сделать тесты для функций
# Разделить на model-view-controller

# user = ['second_name', 'first_name', 'phone_number', 'description']
# phone_dict = {1: ['secondname', 'firstname', 'phone_number', 'description'], 2: ['secondname', 'firstname', 'phone_number', 'description']}

from os.path import join, abspath, dirname

def get_data():
    user=[]
    user.append(input('Введите фамилию: '))
    user.append(input('Введите имя: '))
    user.append(input('Введите номер телефона: '))
    user.append(input('Введите описание: '))
    return user

def create (phone_dict_local: dict, idc: int, user: list):
    idc+=1
    phone_dict_local[idc] = user
    return phone_dict_local, idc

def export_phone_dict(phone_dict: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name+'.txt')
    with open (full_name, mode = 'w', encoding='utf-8') as file:
        for idc, user in phone_dict.items():
            file.write(f'{idc},{user[0]},{user[1]},{user[2]},{user[3]}\n')

def search_user(phone_dict: dict, searching:str):
    for idc, user in phone_dict.items():
        if user[0].startswith(searching):
            return idc, user
    
def delete_user(phone_dict: dict, del_user: str):
    tmp = search_user(phone_dict, del_user)
    if tmp is not None:
        idc, _ = tmp
        phone_dict.pop(idc)
    else:
        print("Человек не найден")
    return phone_dict

def update_user(phone_dict: dict, upd_user: str):
    tmp = search_user(phone_dict, upd_user)
    if tmp is None:
        print ("Человек не найден")
        return phone_dict
    idc, _ = tmp
    new_second_name = input("Введите новую фамилию: ")
    new_first_name = input("Введите новое имя: ")
    new_phone_number = input("Введите новый номер телефона: ")
    new_description = input("Введите новое описание: ")
    if len(new_second_name)>=1:
        phone_dict[idc][0] = new_second_name
    if len(new_first_name)>=1:
        phone_dict[idc][1] = new_first_name
    if len(new_phone_number)>=1:
        phone_dict[idc][2] = new_phone_number
    if len(new_description)>=1:
        phone_dict[idc][3] = new_description
    return phone_dict

def import_phone_dict(phone_dict_local: dict, im_file_name: str, idc: int):
    with open (im_file_name, 'rt') as dict_file:
        for item in dict_file:
            idc +=1
            temp_user = item.strip().split(',')
            phone_dict_local[idc] = temp_user[1:]
        return phone_dict_local, idc

def menu():
    id_user = 0
    phone_dict = dict()
    print('Введите 0, если  хотите выйти')
    print('Введите 1, если  хотите добавить нового человека')
    print('Введите 2, если  хотите распечатать справочник')
    print('Введите 3, если  хотите экспортировать данные')
    print('Введите 4, если  хотите найти данные о человеке')
    print('Введите 5, если  хотите удалить человека')
    print('Введите 6, если  хотите заменить данные о человеке')
    print('Введите 7, если  хотите импортировать данные')
    while True:
        num = int(input('Выберите операцию: '))
        if num == 0 :
            break
        if num == 1:
            user = get_data()
            phone_dict, id_user = create(phone_dict,id_user,user)
        if num == 2:
            print(phone_dict)
        if num == 3:
            file_name = input("Введите имя файла, куда хотите экспортировать справочник: ")
            export_phone_dict(phone_dict, file_name)
        if num == 4:
            searching = input("О ком Вы хотите найти информацию? ")
            id, person = search_user(phone_dict, searching)
            print(f'Вы ищите: {person}, его id в справочнике {id}')
        if num == 5:
            del_user = input("Кого Вы хотите удалить из справочника? ")
            phone_dict = delete_user(phone_dict, del_user)
            print(phone_dict)
        if num == 6:
            upd_user = input ("Информаци о ком Вы хотите изменить? ")
            phone_dict = update_user(phone_dict, upd_user)
            print(phone_dict)
        if num == 7:
            im_file_name = input("Введите имя файла, который хотите импортировать: ")
            phone_dict, id_user = import_phone_dict(phone_dict, im_file_name, id_user)
            print(phone_dict)

# upd_user = "Соколов"
# update_user(phone_dict, upd_user)
# print (phone_dict)

# print(get_data())
# id_user = 0
# phone_dict = dict()
# user1= ['Соколов','Андрей','555444','Зам. директора']
# user2= ['Сыркин','Василий','7523685','Снабженец']
# phone_dict, id_user = create(phone_dict,id_user,user1)
# phone_dict, id_user = create(phone_dict,id_user,user2)
# print(phone_dict)

menu()
# export_phone_dict(phone_dict, 'phones')
