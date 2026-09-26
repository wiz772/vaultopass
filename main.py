import utils.utils as utils
import vault.vault as vault
import core.settings as settings
import core.setup as setup
import core.session as session
import utils.config as config_handler

def show_main_choice():
    print(r""" 

    1. Open Vault
    2. Settings
    3. Exit

""")

def handle_choice(session):
    choices = {
        "1": lambda: vault.open_vault(session),
        "2": settings.show_settings_menu,
        "3": utils.exit_program
    }

    while True:
        show_main_choice()
        choice = input("> ")

        if choice in choices:
            choices[choice]()

def main(): 
    config = config_handler.load_config()
    current_session = session.Session(config["timeout"])

    utils.show_credits()
    handle_choice(current_session)

if __name__ == "__main__":
    setup.check_setup()
    main() 