import sys
phonebook = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func (*args, **kwargs)
        except KeyError:
            return "Контакт з таким ім'ям вже існує."
        except ValueError:
            return "Невірний формат, введіть ім'я та номер телефону"
        except IndexError:
            return "Контакт з таким ім'ям не знайдено."
    return inner

@input_error
def add_contact_input(args):
    if len(args) != 2:
        raise ValueError
    username, phone = args
    if len(phone) != 10 or not phone.isdigit():
        return "Номер телефона повинен складатися з 10 цифр."
    if username in phonebook:
        raise KeyError
    phonebook[username] = phone
    return "Контакт успішно додано."

@input_error
def change_contact_input(args):
    if len(args) != 2:
        raise ValueError 
    username, phone = args
    if len(phone) != 10 or not phone.isdigit():
        return "Номер телефона повинен складатися з 10 цифр."
    elif username not in phonebook:
        raise IndexError
    phonebook[username] = phone
    return f"Номер телефону для '{username}' оновлено."

@input_error
def phone_contact_input(args): 
    if len(args) != 1:
        raise ValueError 
    username = args[0]
    if username not in phonebook:
        raise IndexError
    return f"Номер телефону для '{username}': {phonebook.get(username)}"

def main():
    while True:
        user_input = input("Введіть команду: ")
        command, *args = user_input.strip().lower().split(' ')
        try:
            if command == "hello":
                print("How can I help you?")
            elif command == "add":
                print (add_contact_input(args))
            elif command == "change":
                print (change_contact_input(args))    
            elif command == "phone": 
                print(phone_contact_input(args))
            elif command == "all":
                for username, phone in phonebook.items():
                    print(f"{username}: {phone}")
            elif command in ["close", "exit"]:
                print("Good bye!")
                sys.exit(0)
            else:
                print("Невідома команда. Спробуйте ще раз.")
        except ValueError as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
