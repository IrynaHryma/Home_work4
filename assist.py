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
def greeting(*args):
    for arg in args:
        if arg == "hello":
            return "How can I help you?"
        elif arg == "good bye":
            return "See you soon"

    return "How can I help you?"     # Не знаю,як це змінювати на "See you soon"


@handle_errors
def no_command(*args):
    return "Unknown command"


def parser(text: str) -> tuple[callable, tuple[str] | None]:
    if text.startswith('add'):
        return add, text.replace("add", "").strip().split()
    elif text.startswith('hello'):
        return greeting, (text,)
    elif text.startswith('good bye'):
        return greeting, (text, )
    else:
        return no_command, None


def main():
    while True:
        user_input = input(">>>>")
        command, data = parser(user_input)
        if command is None:
            print("See you soon")
            break
        result = command(data)
        if result is not None:
            print(result)


if __name__ == "__main__":
    main()
