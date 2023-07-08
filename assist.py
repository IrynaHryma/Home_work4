contacts ={}

def handle_errors(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Invalid input. Please enter a valid name and phone number"
        except IndexError:
            return "Invalid input. please try again"
    return wrapper


@handle_errors
def add(*args):
    name,phone = args
    contacts[name] = phone
    return f"Add success {name}, {phone}"


@handle_errors
def greeting(*text):
    return "How can I help you?"
    
@handle_errors
def exit_command (*args):
    return "See you soon"             

@handle_errors
def change (*args):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Phone updated successfully"
    else:
        return "Contact not found"
    
@handle_errors
def phone(*args):
    name = args[0]
    if name in contacts:
        return f"Phone number for{name} is {contacts[name]}"
    else:
        return f" Contact not found"
    
@handle_errors
def show_all(*args):
    if contacts:
        all_cintacts = ""
        for name, phone in contacts.items():
            all_cintacts+=f"{name}:{phone} "
        return all_cintacts
    else:
        return "Contact not found"   


@handle_errors
def no_command(*args):
    return "Unknown command"


COMMANDS = {add: "add",
            greeting: "hello",
            exit_command: "good bye"}


def parser(text: str) -> tuple[callable, tuple[str] | None]:
    # if text.startswith('add'):
    #     return add, tuple(text.replace("add", "").strip().split())
    # elif text.startswith("change"):
    #     return change, tuple(text.replace('change', "").strip().split())
    # elif text.startswith("phone"):
    #     return phone, text.replace ("phone", "").strip()
    # elif text.startswith ("show all"):
    #     return show_all,tuple(text.replace("show all","").strip().split())
    # elif text == 'hello':
    #     return greeting, text
    # elif text =='good bye':
    #     return exit_command,text
    for cmd, kwd in COMMANDS.items():
        if text.lower().startswith(kwd):
            return cmd, text[len(kwd):].strip().split()
    return no_command, None

def main():
    while True:
        user_input = input(">>>>")
        command, data = parser(user_input)
        # if command is None:
        #     print("See you soon")
        #     break
        result = command(*data)
        if result:
            print(result)
        if command == exit_command:
            break

if __name__ == "__main__":
    main()
