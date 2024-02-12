"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

from csv import DictReader, DictWriter
from os.path import exists
def get_user_data():
    first_name = 'Иван'
    last_name = 'Иванов'
    phone_number = 12345
    return first_name, last_name, phone_number

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
file_name = 'phone.csv'
create_file(file_name)

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
print(read_file(file_name))

def write_file(file_name):
    user_data = get_user_data()
    res = read_file(file_name)
    obj = {'Имя': user_data(0), 'Фамилия': user_data(1), 'Телефон': user_data(2)}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def main():
    while True:
        command = input('Введите комманду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл не создан, создайте его. ')
                continue
            print(*read_file(file_name))

main()