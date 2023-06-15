import model
from view import menu, console, text, input_contact, input_find


def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
                console.print_message(text.open_successful)
            case 2:
                model.saved_information()
                console.print_message(text.saved_info)
            case 3:
                console.show_contacts(model.phone_book)
            case 4:
                new_id = model.check_id()
                new = input_contact(text.input_new_contact, new_id)
                model.add_contact(new)
                console.print_message(text.contact_saved(new.get("name")))
            case 5:
                word = input_find(text.search_word)
                result = model.search(word)
                console.show_contacts(result)
            case 6:
                word = input_find(text.search_word)
                result = model.search(word)
                console.show_contacts(result)
                index = input_find(text.input_index)
                new_id = model.check_id()
                new = input_contact(text.input_change_contact, new_id - 1)
                model.change_contact(int(index) - 1, new)
                old_name = model.phone_book[int(index) - 1].get("name")
                console.print_message(text.contact_changed(new.get("name") if new.get("name") else old_name))
            case 7:
                console.print_message(text.delete_contact)
                word = input_find(text.search_word)
                result = model.search(word)
                console.show_contacts(result)
                index = input_find(text.input_index)
                name = model.delete_contact(int(index))
                model.rearrange_id()
                console.print_message(text.contact_deleted(name))
            case 8:
                break
