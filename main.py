from phonebook_helpers import get_contact_fio, delete_contact, add_contact, print_contact_list, \
    is_valid_contact_index, get_contact_by_index, change_contact


def get_contact_info_submenu(contact_index: int) -> None:
    contact = get_contact_by_index(contact_index)
    fio = get_contact_fio(contact)

    print("")
    print(f"----- {fio} ------")
    print("1. Изменить")
    print("2. Удалить")
    print("3. Выйти")
    print("-----------------------------")
    option = int(input(">>"))

    if option == 1:
        first_name = input("Введите имя:")
        last_name = input("Введите фамилию:")
        change_contact(contact_index, last_name, first_name)

    elif option == 2:
        delete_contact(contact_index)

    elif option == 3:
        get_contacts_submenu()

    else:
        get_contact_info_submenu(contact_index)


def get_contacts_submenu() -> None:
    print("")
    print("----- Список контактов ------")
    contact_count = print_contact_list()
    print(f"{contact_count + 1}. Выйти")
    print("-----------------------------")
    option = int(input(">>"))

    if option == contact_count + 1:
        return

    if is_valid_contact_index(option):
        get_contact_info_submenu(option)
    else:
        print("Выбран неверный пункт меню!")
        get_contacts_submenu()


def menu() -> None:
    print("-----------------------------")
    print("1. Список контактов")
    print("2. Добавить контакт")
    print("3. Удалить контакт")
    print("4. Выйти")
    print("-----------------------------")


def main():
    while True:
        menu()
        option = int(input(">>"))
        print("")

        if option == 1:
            get_contacts_submenu()

        elif option == 2:
            first_name = input("Введите имя:")
            last_name = input("Введите фамилию:")
            add_contact(last_name, first_name)

        elif option == 3:
            print("Удаление контактов:")
            print_contact_list()
            index = int(input("Введите номер контакта который хотите удалить: "))

            delete_contact(index)
        elif option == 4:
            break
        else:
            print("Выбран неверный пунк меню")

        print("")


if __name__ == "__main__":
    main()
