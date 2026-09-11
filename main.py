import utils

def show_main_choice():
    print(r""" 

    1. Open Vault
    2. Settings
    3. Exit

""")

def add():
    print("a")

def handle_choice():
    choices = {
        "1": add,
        "2": add,
        "3": utils.exit_program
    }

    while True:
        choice = input("> ")

        if choice in choices:
            choices[choice]()

def main(): 
    utils.show_credits()
    show_main_choice()
    handle_choice()

if __name__ == "__main__":
    main() 