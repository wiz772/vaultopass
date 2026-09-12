import utils.utils as utils
import vault.vault as vault
import core.settings as settings
import core.setup as setup

def show_main_choice():
    print(r""" 

    1. Open Vault
    2. Settings
    3. Exit

""")

def handle_choice():
    choices = {
        "1": vault.open_vault,
        "2": settings.show_settings_menu,
        "3": utils.exit_program
    }

    while True:
        show_main_choice()
        choice = input("> ")

        if choice in choices:
            choices[choice]()

def main(): 
    utils.show_credits()
    handle_choice()

if __name__ == "__main__":
    setup.check_setup()
    main() 