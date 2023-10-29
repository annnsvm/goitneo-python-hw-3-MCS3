import task1
from task2 import AddressBook


def main():
    address_book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = task1.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(task1.add_contact(args, address_book))
        elif command == "change":
            print(task1.change_contact(args, address_book))
        elif command == "remove":
            print(task1.delete_contact(args, address_book))
        elif command == 'phone':
            print(task1.show_contact(args, address_book))
        elif command == "all":
            print(task1.show_all(address_book))
        elif command == "add-birthday":
            print(task1.add_birthday(args, address_book))
        elif command == "show-birthday":
            print(task1.show_birthday(args, address_book))
        elif command == "birthdays":
            print(task1.get_birthdays_per_week(address_book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
