from utils import utils

def ask_password():
    password = input("Enter your master password: ")
    return password

def vault_loop(session):
    utils.clear_console()
    while session.is_unlocked():
        input("Vault is unlocked. Press Enter to lock the vault and exit...")
        close_vault(session)

def open_vault(session):
    if not session.is_unlocked():

        password = ask_password()

        if not session.unlock(password):
            print("Failed to unlock your session. Your vault is still sealed.")
            return

    utils.setting_window_name("VaultoPASS - Vault")
    vault_loop(session)

def update_vault(session, data):
    ...

def close_vault(session):
    session.lock()