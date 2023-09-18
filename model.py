


def create_rec (id: object, name: object, note_body: object, data_time: object)->dict:
    """
    Функция создает новую заметку
    :param id: идентификатор заметки
    :param name: заголовок заметки
    :param note_body: тело заметки
    :param data_time: дата/время создания заметки
    :return: запись в виде словаря
    """
    return {'id': id, 'name': name, 'note_body': note_body, 'data_time': str(data_time)}

def select (note_book: list, id: str)->list:
    """
    Выбор записи по фильтру даты/времени
    :param note_book: Список заметок
    :param template: шаблон для поиска даты/времени
    :return:
    """
    return [rec for rec in note_book if rec['id'].startswith(id)]

def merge(new_rec: dict, old_rec: dict) -> dict:
    """
    Добавляет заметку к уже имеющейся, меняется дата и содержимое заметки
    :param new_rec: Новая заметка (возможно с пустыми полями)
    :param old_rec: Старая заметка (без пустых полей)
    :return: Запись слитая из двух
    """
    return {'id': old_rec['id'], 'name': new_rec['name'] if new_rec['name'] != "" else old_rec ['name'], 'note_body': old_rec['note_body']+"\n"+new_rec['note_body'], 'data_time':  new_rec['data_time']}


def import_file(filename: str, delimiter=";") -> list:
    """
    Чтение заметки из файла
    :param filename:  имя файла(текущая директория)
    :param delimiter: Разделитель полей
    :return: Список словарей(записей)
    """
    rez = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            id, name, note_body, data_time = line.strip().split(delimiter)
            rez.append({'id': id, 'name': name, 'note_body':note_body, 'data_time': data_time})
    return rez


def export_file(filename: str, note_book: list, delimiter=";"):
    """
    запись заметкии в файл
    :param filename: имя файла(текущая директория)
    :param note_book: Справочник(список словарей)
    :param delimiter: Разделитель полей
    :return: None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        for rec in note_book:
            file.write(";".join(rec.values()))
            file.write(f"\n")
