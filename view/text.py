main_menu = """Главное меню
    1. Открыть Файл
    2. Сохранить файл
    3. Показать контакт
    4. Создать новый контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход. \n"""
menu_choice = "Выберите пункт меню: "
input_error = "Некорректный ввод! Введите от 1 до 9."
book_error = "Телефонный справочник пуст или файл не открыт"
open_successful = "Телефонная книга открыта"
for_name = "\nВведите ФИО/ФИ лица: "
for_phone = "\nВведите номер лица: "
for_comment = "\nВведите комментарий к лицу: "
input_new_contact = "\nВведите новые данные: "
search_word = "Искомый элемент: "
input_index = "Введите индекс искомого контакта: "
input_change_contact = "Введите данные изменяемого контакта или Enter? чтобы оставить дефолт: "
saved_info = "Файл успешно сохранён!"
delete_contact = "Хотите удалить контакт?"
fulled_contacts = "Контакт уже открыт."

def contact_saved(name: str):
    return f"Контакт {name} успешно сохранён."


def contact_changed(name: str):
    return f"Контакт {name} успешно изменён."


def contact_deleted(name: str):
    return f"Контакт {name} удалён."
