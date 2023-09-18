import datetime as d


def new_rec(mode="new") ->tuple:
    """
    ВВод данных для новой записи в заметки
    :param mode:
    :return: Данные записи в виде кортежа
    """

    if mode == "new":
        print("Режим создания заметки")
        id = input("Введите id заметки: ")
        name = input("Введите название заметки: ")
        note_body = input("Введите текст заметки: ")
    elif mode == "update":
        print("Ввод новых данных для записи ")
        print("Пустая строка означает оставить данные без изменения")
        name = input("Введите новое название заметки: ")
        note_body = input("Введите текст для добавления в заметку : ")
        id=""
    else:
        raise ValueError(f"Недопустимый флаг mode: {mode}")
    # id = input("Введите id заметки: ")
    # name = input("Введите название заметки: ")
    # note_body = input("Введите текст заметки: ")
    data_time = d.datetime.now()
    print (data_time)
    return id, name,  note_body, data_time

def file_name_r ()->str:
    """
    Возвращает имя файла для чтения
    :return: имя файла
    """
    return input("Введите имя файла для чтения: ")

def file_name_w ()->str:
    """
    Возвращает имя файла для сохранения
    :return: имя файла
    """
    return input("Введите имя файла для записи: ")

def id()->str:
    return input ("Введите id заметки: ")

# def show_recs(recs: list):
#     for rec in recs:
#         show_rec(rec)


def show_rec(rec: dict):
    """
    Отображение одной записи в консоли
    :param rec: Запись
    :return: None
    """
    for val in rec.values():
        print(val)
    print("")


def show_all_recs(phone_book: list):
    """
    Отображение всех записей справочника в консоли
    :param phone_book: Справочник
    :return: None
    """
    print("Все заметки: ")
    for rec in phone_book:
        show_rec(rec)


def show_menu() -> str:
    """
    Отображение меню пользователя
    :return:
    """
    print("*"*20)
    print("МЕНЮ:")
    print("\t(c)reate - Создание новой заметки")
    print("\t(r)ead   - Поиск заметки по дате/времени")
    print("\t(u)date  - Изменение заметки")
    print("\t(d)elete - Удаление заметки")
    print("\t(i)mport - Чтение заметки из файла")
    print("\t(e)xport - Запись заметки в файл")
    print("\t(s)how   - Вывод всех заметок")
    print("\t(o)utput - Выход")
    return input("Выберите нужный пункт: ")

