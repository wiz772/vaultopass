from getpass import getpass
from utils import config
from vault import vault_creation

def setup_dialogue():
    print("""
========================================
          Welcome to Vaultopass
========================================

Vaultopass is being configured for the
first time.

You will now configure:
- Master password
- Vault settings

Your master password will be required
to access your vault.

IMPORTANT:
Keep your master password safe.
It cannot be recovered if lost.
""")

    input("Press Enter to continue...")


def ask_masterpassword():
    print("\n--- Master Password ---")
    print("""
Your master password protects your vault.

IMPORTANT:
- Do not forget this password.
- Vaultopass cannot recover it for you.
- Do not store it in your vault.
""")

    while True:
        password = getpass("Enter master password: ")

        if not password:
            print("Password cannot be empty.")
            continue

        confirmation = getpass("Confirm master password: ")

        if password != confirmation:
            print("Passwords do not match. Try again.\n")
            continue

        print("Master password configured.")
        return password


def ask_settings():
    print("\n--- Vault Settings ---")

    default_timeout = 30

    print(f"""
Session timeout controls how long the
vault can remain unlocked before the
session is locked again.

Default: {default_timeout} minutes
""")

    while True:
        timeout_input = input(f"Session timeout in minutes [{default_timeout}]: ").strip()

        if not timeout_input:
            timeout = default_timeout
            break

        try:
            timeout = int(timeout_input)

            if timeout <= 0:
                print("Timeout must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    print(f"\nSession timeout: {timeout} minutes")

    return timeout

def setup():
    setup_dialogue()

    master_password = ask_masterpassword()
    settings = ask_settings()

    config.create_config(settings)
    vault_creation.create_vault(master_password)

def check_setup():
    if not config.config_exists():
        setup()