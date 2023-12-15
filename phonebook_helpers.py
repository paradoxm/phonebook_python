import uuid
from typing import List

from phonebook_types import Contact
from store import get_store_value, set_store_value


def get_contact_list() -> List[Contact]:
    store_value = get_store_value()
    return store_value.get("contacts", [])


def print_contact_list() -> int:
    contact_list = get_contact_list()
    for index, contact in enumerate(get_contact_list()):
        fio = get_contact_fio(contact)
        print(f"{index + 1}. {fio}")

    return len(contact_list)


def get_contact_fio(contact: Contact) -> str:
    first_name = contact.get("first_name", "")
    last_name = contact.get("last_name", "")
    return f"{first_name} {last_name}"


def is_valid_contact_index(index: int) -> bool:
    store_value = get_store_value()
    contacts = store_value.get("contacts", [])
    return 0 < index <= len(contacts)


def get_contact_by_index(index: int) -> Contact:
    store_value = get_store_value()
    contacts = store_value.get("contacts", [])
    return contacts[index - 1]


def delete_contact(index: int) -> None:
    store_value = get_store_value()
    contacts = store_value.get("contacts", [])

    if not is_valid_contact_index(index):
        print(f"Не удалось удалить. Контакта с нмоером {index} не существует!")
        return

    contact_id = contacts[index - 1]["id"]
    new_contacts = [contact for contact in contacts if contact["id"] != contact_id]
    store_value["contacts"] = new_contacts
    set_store_value(store_value)


def add_contact(last_name: str, first_name: str) -> None:
    contact = Contact(id=str(uuid.uuid4()), first_name=first_name, last_name=last_name)
    value = get_store_value()
    value["contacts"].append(contact)
    set_store_value(value)


def change_contact(index: int, last_name: str, first_name: str) -> None:
    if not is_valid_contact_index(index):
        print(f"Не удалось изменить. Контакта с нмоером {index} не существует!")
        return

    store_value = get_store_value()
    contact = store_value["contacts"][index - 1]
    contact["first_name"] = first_name
    contact["last_name"] = last_name
    store_value["contacts"][index - 1] = contact
    set_store_value(store_value)
