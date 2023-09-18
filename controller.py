import view
import model



def menu():
    """
    Функция обработки меню
    :return: None
    """
    note_book_main = []
    while True:
        choice = view.show_menu()
        if choice == "o" or choice == "щ":
            print("до новых встреч")
            break
        elif choice == "c" or choice == "с":
            rec = model.create_rec(*view.new_rec(mode = "new"))
            note_book_main.append(rec)
        elif choice == "r" or choice == "к":
            id = view.id()
            recs = model.select(note_book_main, id)
            view.show_all_recs(recs)
        elif choice == "u" or choice == "г":
            id = view.id()
            recs = model.select(note_book_main, id)
            if recs:
                idx = note_book_main.index(recs[0])
                rec = model.create_rec(*view.new_rec(mode = "update"))
                rec = model.merge(rec, recs[0])
                note_book_main[idx] = rec
        elif choice == "d" or choice == "в":
            id = view.id()
            recs = model.select(note_book_main, id)
            if recs:
                idx = note_book_main.index(recs[0])
                note_book_main.pop(idx)
        elif choice == "i" or choice == "ш":
            filename = view.file_name_r()
            recs = model.import_file(filename)
            note_book_main.extend(recs)
        elif choice == "e" or choice == "у":
            filename = view.file_name_w()
            model.export_file(filename, note_book_main)
        elif choice == "s" or choice == "ы":
            view.show_all_recs(note_book_main)
        else:
            print("Недопустимый пункт меню")