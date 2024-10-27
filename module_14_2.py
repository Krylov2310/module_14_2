import sqlite3

print('\033[30m\033[47mДомашнее задание по теме "Выбор элементов и функции в SQL запросах""\033[0m')
print('\033[30m\033[47mЦель: научится использовать функции внутри запросов языка SQL и использовать их в '
      'решении задачи.\033[0m')
print('\033[30m\033[47mЗадача "Средний баланс пользователя":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
print('\033[30m\033[47mДата: 27.10.2024г.\033[0m')
thanks = '\033[47mБлагодарю за внимание :-)\033[0m'
print()

file_name = 'not_telegram.db'
full_table = ''
base_names = ''
connection = sqlite3.connect(file_name)
cursor = connection.cursor()
quantity = 11


def create_a_database(base_name, user_name, mail_name, age_name, balance_name):
    global full_table
    global base_names
    global connection
    global cursor
    print(f'\033[32mСоздаем базу данных, если она существует, то открываем: {file_name}\033[0m')
    base_names = base_name
    full_table = user_name, mail_name, age_name, balance_name
    print(f'\033[34mСоздаем список таблиц - Пользователь: {base_name}, поля: {user_name}, {mail_name}, {age_name}, '
          f'{balance_name}\033[0m')
    set_file_name = (f'''CREATE TABLE IF NOT EXISTS {base_name}(
            id INTEGER PRIMARY KEY,
            {user_name} TEXT NOT NULL,
            {mail_name} TEXT NOT NULL,
            {age_name} INTEGER,
            {balance_name} INT NOT NULL
        )
    ''')
    cursor.execute(set_file_name)


def fill_in_the_table(set_name, set_email, set_dog, set_age, set_balance):
    global full_table
    global base_names
    global connection
    global cursor
    for i in range(1, quantity):
        j = str(i)
        set1 = str(f'INSERT INTO {base_names} ({full_table[0]}, {full_table[1]}, {full_table[2]}, '
                   f'{full_table[3]}) VALUES (?, ?, ?, ?)')
        set2 = str(f"{set_name}{j}")
        set3 = str(f'{set_email}{j}{set_dog}')
        set4 = int(set_age)
        set5 = int(set_balance)
        cursor.execute(f'{set1}', (f'{set2}', f'{set3}', set4, set5))
        set_age += 10
    print(f'\033[31mЗаполнили список {quantity - 1}ю записями:\033[0m')
    # display()


def update_balance(quantity_b, plus_b):
    global full_table
    global base_names
    global connection
    global cursor
    global quantity
    for bal in range(1, quantity):
        if not (bal - 1) % quantity_b:
            set1 = str(f'UPDATE {base_names} SET {full_table[3]} = {plus_b} WHERE  id = ?')
            cursor.execute(f'{set1}', (bal,))
    print(f'\033[31mОбновили баланс у каждой {quantity_b}й записи начиная с 1й на {plus_b}:\033[0m')
    # display()


def delete_table(quantity_t):
    global full_table
    global base_names
    global connection
    global cursor
    for dell in range(1, quantity):
        if not (dell - 1) % quantity_t:
            set1 = str(f'DELETE FROM {base_names} WHERE  id = ?')
            cursor.execute(f'{set1}', (dell,))
    print(f'\033[31mУдалили каждую {quantity_t}ю запись в таблице начиная с 1й:\033[0m')
    # display()


def old_users(set_old):
    global full_table
    global base_names
    global connection
    global cursor
    set1 = str(f'SELECT {full_table[0]}, {full_table[1]}, {full_table[2]}, {full_table[3]} FROM {base_names} '
               f'WHERE  {full_table[2]} != ?')
    cursor.execute(f'{set1}', (set_old,))
    users = cursor.fetchall()
    print(f'\033[31mВыборка по записям, где возраст не равен: {set_old}\033[0m')
    for old_ in users:
        print(f'Имя: {old_[0]}| Почта: {old_[1]}| Возраст: {old_[2]}| Баланс: {old_[3]}')


def delete_one(del_o):
    global full_table
    global base_names
    global connection
    global cursor
    set1 = str(f'DELETE FROM {base_names} WHERE  id = ?')
    cursor.execute(f'{set1}', (del_o,))
    print(f'\033[31mУдалили {del_o}ю запись в таблице:\033[0m')
    display()


def all_users():
    global full_table
    global base_names
    global connection
    global cursor
    set1 = str(f'SELECT COUNT(*) FROM {base_names}')
    cursor.execute(f'{set1}')
    total_user = cursor.fetchone()[0]
    print(f'Количество всех пользователей: \033[31m{total_user} \033[0m')
    set2 = str(f'SELECT SUM({full_table[3]}) FROM {base_names}')
    cursor.execute(f'{set2}')
    all_balance = cursor.fetchone()[0]
    average_balance = int(all_balance) / int(total_user)
    print(f'Общая сумма всех балансов SUM: \033[31m{all_balance} \033[0m')
    print(f'Средняя сумма всех балансов SUM: {all_balance} / {total_user} = \033[31m{average_balance} \033[0m')
    set3 = str(f'SELECT AVG({full_table[3]}) FROM {base_names}')
    cursor.execute(f'{set3}')
    all_balance2 = cursor.fetchone()[0]
    print(f'Средняя сумма всех балансов AVG: \033[31m{all_balance2} \033[0m')


def display():
    global base_names
    cursor.execute(f'SELECT * FROM {base_names}')
    users = cursor.fetchall()
    for user in users:
        print(user)


def finish():
    global connection
    global cursor
    connection.commit()
    connection.close()


if __name__ == '__main__':
    create_a_database('Users', 'username', 'email',
                      'age', 'balance')
    # create_a_database('Users_2024', 'Имя', 'email',
    #                   'Возраст', 'Баланс')
    fill_in_the_table('User', 'example',
                      '@gmail.com', 10, 1000)
    update_balance(2, 500)
    delete_table(3)
    # old_users(60)
    delete_one(6)
    print()
    all_users()
    finish()
    print()
    print(thanks)
