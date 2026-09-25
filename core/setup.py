import os
from getpass import getpass


def setup_dialogue():
    print("""
========================================
          Welcome to Vaultopass
========================================

Vaultopass is being configured for the
first time.

You will now configure:
- Vault storage location
- Master password
- Vault settings

Your master password will be required
to access your vault.

IMPORTANT:
Keep your master password safe.
It cannot be recovered if lost.
""")

    input("Press Enter to continue...")


def ask_storage_path():
    default_path = os.path.expanduser("~/.vaultopass")

    print("\n--- Vault Storage ---")
    print("Where would you like to store your vault?")
    print(f"Press Enter to use the default path:")
    print(f"  {default_path}")

    path = input("\nStorage path: ").strip()

    if not path:
        path = default_path

    path = os.path.abspath(os.path.expanduser(path))

    print(f"\nVault will be stored in:")
    print(f"  {path}")

    while True:
        confirm = input("Is this correct? [Y/n]: ").strip().lower()
        if confirm in ("", "y", "yes"):
            break
        if confirm in ("n", "no"):
            return ask_storage_path()
        print("Please enter Y or N.")

    return path


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
        timeout_input = input(
            f"Session timeout in minutes [{default_timeout}]: "
        ).strip()

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

def write_config(config):
    ...

def create_config(storage_path, settings):
    timeout = settings

    config = {
        "version": 1,
        "storage_path": storage_path,
        "timeout": timeout
    }

    write_config(config)

    return config


def create_vault(path, master_password, config):
    ...


def setup():
    setup_dialogue()

    storage_path = ask_storage_path()
    master_password = ask_masterpassword()
    settings = ask_settings()

    config = create_config(storage_path, settings)
    create_vault(storage_path, master_password, config)


def config_exists():
    return False


def check_setup():
    if not config_exists():
        setup()