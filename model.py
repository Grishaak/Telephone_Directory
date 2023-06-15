phone_book = []
path = "phone.txt"


def open_file():
    if not phone_book:
        with open(path, "r", encoding="utf-8") as file:
            data = file.readlines()
            for contact in data:
                user_id, name, phone, comment, *_ = contact.strip().split(":")
                phone_book.append({"id": user_id, "name": name, "phone": phone, "comment": comment})


def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get("id")))
    return max(uid_list) + 1


def add_contact(new: dict):
    new.update({"id": check_id()})
    phone_book.append(new)


def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for value in contact.values():
            if word.lower() in str(value).lower():
                result.append(contact)
                break
    return result


def change_contact(index: int, new: dict[str, str]):
    for key, value in new.items():
        if value != "":
            phone_book[index][key] = value


def saved_information():
    with open(path, "w", encoding="utf-8") as file:
        for info in phone_book:
            new_info = ":".join(str(i) for i in info.values()) + '\n'
            file.write(new_info)
        # file.close()


def delete_contact(index: int):
    for contact in phone_book:
        if str(index) == str(contact.get("id")):
            del_name = contact.get("name")
            del phone_book[int(contact.get("id")) - 1]
    return del_name


def rearrange_id():
    for new_id in range(len(phone_book)):
        phone_book[new_id].update({"id": new_id + 1})
