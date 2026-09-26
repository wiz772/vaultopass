from utils import utils
from vault import vault
from core import settings
from core import setup
from core import session
from utils import config as config_handler

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
        utils.setting_window_name("VaultoPASS - Menu")

        show_main_choice()
        choice = input("> ")

        if choice in choices:
            choices[choice]()


def get_session():
    config = config_handler.load_config()
    current_session = session.Session(config["timeout"])
    return current_session

def start(current_session):
    utils.show_credits()
    handle_choice(current_session)

def main(): 
    current_session = get_session()
    start(current_session)

if __name__ == "__main__":
    setup.check_setup()
    main() 