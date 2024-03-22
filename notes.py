import datetime


def get_id():
    with open("notebook.csv", "r", encoding="UTF-8") as file:
        text = file.read()
        if len(text) == 0:
            return 1
        note_list = text.rstrip().split("\n\n\n")
    return len(note_list)+1


def get_title():
    new_title = ""
    while len(new_title) == 0:
        new_title = input("Введите заголовок заметки:\n").strip()
    return new_title


def get_date():
    return datetime.datetime.now()


def get_note():
    new_note = ""
    while len(new_note) == 0:
        new_note = input("Введите свою заметку:\n").strip()
    return new_note


def create_note():
    return f"{get_id()}\n{get_title()}\n{get_date()}\n{get_note()}\n\n\n"


def add_note():
    note = create_note()
    with open("notebook.csv", "a", encoding="UTF-8") as file:
        file.write(note)


def show_all_notes():
    with open("notebook.csv", "r", encoding="UTF-8") as file:
        all_notes = file.read()
        print(all_notes)

    # если пусто - написать, что пусто?


def search_note():
    case_search = input(
        "Введите вариант поиска:\n"
        "1. По заголовку.\n"
        "2. По дате.\n"
        "3. По тексту.\n"
        "Ваш выбор: "
    )

    while case_search not in ("1", "2", "3"):
        print("Некорректный ввод данных")
        case_search = input("Выберите вариант поиска: ")

    index_serch = int(case_search)
    search = input("Введите информацию для поиска: ")

    with open("notebook.csv", "r", encoding="UTF-8") as file:
        note_list = file.read().rstrip().split("\n\n\n")
        for note_str in note_list:
            cur_note = note_str.split("\n")
            if search in cur_note[index_serch]:
                print(note_str)


def edit_note():
    with open("notebook.csv", "r+", encoding="UTF-8") as file:
        text = file.read()
        if len(text) == 0:
            print("Заметки для редактирования отсутствуют.")
            return
        note_list = text.rstrip().split("\n\n\n")
        note_list_size = len(note_list)
        print(f"Всего на данный момент заметок: {note_list_size}.")
        id_list = [str(i+1) for i in range(note_list_size)]
        edit_id = "0"
        while edit_id not in id_list:
            edit_id = input("Введите номер заметки для редактирования: ")
        edit_note=note_list[int(edit_id)-1]
        list_edit_note=edit_note.split("\n")
        new_note=""
        while len(new_note) == 0:
            print(f"Старый текст заметки:\n{list_edit_note[3]}")
            new_note = input("Введите новый текст заметки:\n").strip()
        list_edit_note[3]=new_note
        note_list[int(edit_id)-1]=""
        for i in range(len(list_edit_note)):
            note_list[int(edit_id)-1]+=f"{list_edit_note[i]}\n"
        note_list[int(edit_id)-1]=note_list[int(edit_id)-1].strip()
        text = ""
        for i in range(len(note_list)):
            text += note_list[i]+"\n\n\n"
    with open("notebook.csv", "w", encoding="UTF-8") as file:
        file.write(text)


def delete_note():
    with open("notebook.csv", "r+", encoding="UTF-8") as file:
        text = file.read()
        if len(text) == 0:
            print("Заметки для удаления отсутствуют.")
            return
        note_list = text.rstrip().split("\n\n\n")
        note_list_size = len(note_list)
        print(f"Всего на данный момент заметок: {note_list_size}.")
        id_list = [str(i+1) for i in range(note_list_size)]
        del_id = "0"
        while del_id not in id_list:
            del_id = input("Введите номер заметки для удаления: ")
        note_list.pop(int(del_id)-1)
        for i in range(len(note_list)):
            cur_note = note_list[i].split("\n")
            cur_note[0] = str(i+1)
            note_list[i] = ""
            for j in range(len(cur_note)):
                note_list[i] += f"{cur_note[j]}\n"
        text = ""
        for i in range(len(note_list)):
            text += note_list[i]+"\n\n"
    # print(text)
    with open("notebook.csv", "w", encoding="UTF-8") as file:
        file.write(text)


def interface():
    menu_param = "0"
    with open("notebook.csv", "a", encoding="UTF-8") as file:
        pass
    while menu_param != "6":
        print("""Возможные действия:
            1. Вывести все заметки. 
            2. Добавить заметку.
            3. Поиск заметки.
            4. Редактировать заметку.
            5. Удалить заметку.
            6. Выход.
            """)
        menu_param = input("Выберите пункт меню: ")
        while menu_param not in ("1", "2", "3", "4", "5", "6"):
            print("Выберите пункт меню: ")
            menu_param = input()
        match menu_param:
            case "1":
                show_all_notes()
            case "2":
                add_note()
            case "3":
                search_note()
            case "4":
                edit_note()
            case "5":
                delete_note()
            case "6":
                print("Всего доброго.")


print()
interface()
