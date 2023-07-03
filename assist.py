def handle_errors(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            return f"Error: {str(e)}"
    return wrapper


@handle_errors
def add(*args):
    # # if len(*args) < 2:
    #     return "Error"
    name = args[0]
    phone = args[1]
    return f"Add success {name}, {phone}"


@handle_errors
def greeting(text):
    if text in ["hello","good morning"]:
        return "How can I help you?"
    else:
        return "See you soon"                 #Не знаю,як змінити відповідь "Hello" - "How can I helpl you?"

@handle_errors
def no_command(*args):
    return "Unknown command"


def parser(text: str) -> tuple[callable, tuple[str] | None]:
    if text.startswith('add'):
        return add, text.replace("add", "").strip().split()
    elif text == 'hello':
        return greeting, (text,)
    elif text =='good bye':
        return greeting, (text, )
    else:
        return no_command, None


def main():
    while True:
        user_input = input(">>>>")
        command, data = parser(user_input)
        if command is None:
            print("See you soon!")
            break
        result = command(data)
        if result is not None:
            print(result)


if __name__ == "__main__":
    main()
