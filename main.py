# Декоратор для обробки помилок вводу
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"

    return wrapper


class AssistantBot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def hello_command(self):
        return "How can I help you?"

    @input_error
    def add_command(self, data):
        # Розділення введених даних на ім'я та номер телефону
        name, phone = data.split()
        # Забезпечення того, що ім'я починається з великої літери
        name = name.capitalize()
        # Збереження контакту
        self.contacts[name] = phone
        return f"Contact {name} added with phone {phone}"

    @input_error
    def change_command(self, data):
        # Розділення введених даних на ім'я та номер телефону
        name, phone = data.split()
        # Забезпечення того, що ім'я починається з великої літери
        name = name.capitalize()
        # Оновлення номера телефону для існуючого контакту
        self.contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"

    @input_error
    def phone_command(self, name):
        # Забезпечення того, що ім'я починається з великої літери
        name = name.capitalize()
        # Виведення номера телефону для зазначеного контакту
        return f"Phone number for {name}: {self.contacts[name]}"

    @input_error
    def show_all_command(self):
        # Виведення всіх збережених контактів
        return "Contacts:\n" + "\n".join(f"{name}: {phone}" for name, phone in self.contacts.items())

    def process_command(self, command):
        # Розбиття введеної команди на окремі частини
        parts = command.lower().split()
        if not parts:
            return "Invalid command. Please try again."

        # Визначення дії з першої частини команди
        action = parts[0]

        if action == "hello":
            return self.hello_command()
        elif action == "add":
            if len(parts) == 3:
                return self.add_command(parts[1] + " " + parts[2])
            else:
                return "Invalid 'add' command. Usage: add [name] [phone]"
        elif action == "change":
            if len(parts) == 3:
                return self.change_command(parts[1] + " " + parts[2])
            else:
                return "Invalid 'change' command. Usage: change [name] [phone]"
        elif action == "phone":
            if len(parts) == 2:
                return self.phone_command(parts[1])
            else:
                return "Invalid 'phone' command. Usage: phone [name]"
        elif action == "show" and parts[-1] == "all":
            return self.show_all_command()
        elif action in ["goodbye", "close", "exit"]:
            return "Good bye!"
        else:
            return "Unknown command. Please try again."


def main():
    bot = AssistantBot()

    print("Welcome to the Assistant Bot!")
    print("Commands:")
    print("1. hello")
    print("2. add [name] [phone]")
    print("3. change [name] [phone]")
    print("4. phone [name]")
    print("5. show all")
    print("6. exit / close / goodbye")

    while True:
        user_input = input("\nEnter your command: ")
        response = bot.process_command(user_input)
        print(response)

        if response.lower() in ["good bye!", "exit", "close"]:
            break


if __name__ == "__main__":
    main()

