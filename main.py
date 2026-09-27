from utils import utils
from vault import vault
from core import settings
from core import setup
from core.session import Session
from utils import config as config_handler

def show_main_choice():
    print(r""" 

    1. Open Vault
    2. Settings
    3. Exit

""")

def main_menu_visuals():
    utils.clear_console()
    utils.setting_window_name("VaultoPASS - Menu")
    utils.show_credits()

def handle_choice(session: Session):
    choices = {
        "1": lambda: vault.open_vault(session),
        "2": settings.show_settings_menu,
        "3": utils.exit_program
    }

    while True:
        main_menu_visuals()
        show_main_choice()

        choice = input("> ")

        if choice in choices:
            choices[choice]()


def get_session():
    config = config_handler.load_config()
    current_session = Session(config["timeout"])
    return current_session

def start(current_session: Session):
    handle_choice(current_session)

def main(): 
    current_session = get_session()
    start(current_session)

if __name__ == "__main__":
    setup.check_setup()
    main() 