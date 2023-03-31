def id_():
    id_note = int(input("Входной идентификатор заметки\n"))
    
    if id_note > 0:
        return id_note
    else:
        print("Извините, я ничего не могу найти. Для первой ноты:")
        return 1


def output(value):
    print(value)


def note():
    name = input("Введите название:\n")
    body = input("Введите сообщение:\n")
    return name, body


def help():
    answer = input("Вы потеряли файл 'notes.json'? yes/no\n")
    if answer == 'yes':
        return True
    else:
        return False

def start_menu():
    option = int(input("1. Прочитайте все\n2. Прочтите заметку\n3. Добавь\n4. Редактировать\n5. Удалить\n6. ПОМОЩЬ!\n7. Выход\n"))
    if option in [1, 2, 3, 4, 5, 6, 7]:
        return option
    else: print("Извините, не могли бы вы повторить, пожалуйста?")

def id_or_time():
    opt = int(input("Как бы вы хотели видеть заметки? идентификатор (1) или время (2)?\n"))
    if opt == 1:
        return True
    else: return False