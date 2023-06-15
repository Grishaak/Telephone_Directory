from .text import *


def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print(input_error)


def show_contacts(book: list[dict[str, str]]):
    if book:
        length = max([len("".join(list(str(item.values())))) for item in book])+30
        print("\n" + "=" * int(length))
        for contact in book:
            uid = contact.get("id")
            name = contact.get("name")
            phone = contact.get("phone")
            comment = contact.get("comment")
            print(f"{uid:>3}. {name:<20} {phone:<20} {comment:<20}")
        print("=" * int(length) + "\n")
    else:
        print(book_error)


def print_message(message: str):
    length = len(message)
    print("\n" + "=" * length)
    print(message)
    print("=" * length + "\n")


def input_contact(message: str, uid: str) -> dict[str, str]:
    print(message)
    name = input(for_name)
    phone = input(for_phone)
    comment = input(for_comment)
    return {"id": uid, "name": name, "phone": phone, "comment": comment}


def input_find(message: str) -> str:
    return input(message)
