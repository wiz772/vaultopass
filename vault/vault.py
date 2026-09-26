from utils import utils

def ask_password():
    password = input("Enter your master password: ")
    return password

def vault_main_menu():
    print(r"""

\ \ / /  /_\   | | | | | |  |_   _|
 \ V /  / _ \  | |_| | | |__  | |  
  \_/  /_/ \_\  \___/  |____| |_|
───────────────────────────────────

1. View entries
2. Add entry
3. Edit entry
4. Delete entry
5. Lock vault

───────────────────────────────────
""")

def vault_show_entries(vault_data):
    entries = vault_data.get("entries", [])
    if not entries:
        print("No entries found in the vault.")
        return

    print("\nENTRIES:")
    for i, entry in enumerate(entries, start=1):
        print(f"{i}. {entry['name']} - {entry['username']}")

def vault_loop(session):
    utils.clear_console()

    choices = {
            "1": lambda: vault_show_entries(session.vault_data),
            "2": ...,
            "3": ...,
            "4": ...,
            "5": lambda: close_vault(session)
    }

    while session.is_unlocked():
        vault_main_menu()
        choice = input("> ")
        if choice in choices:
            choices[choice]()


def open_vault(session):
    if not session.is_unlocked():

        password = ask_password()

        if not session.unlock(password):
            print("Failed to unlock your session. Your vault is still sealed.")
            return

    utils.setting_window_name("VaultoPASS - Vault")
    vault_loop(session)

def update_vault(session, data):
    print("Updating vault data...")

def close_vault(session):
    session.lock()