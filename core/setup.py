def setup_masterpassword():
    ...

def setup_dialogue():
    ...

def ask_storage_path():
    ...

def ask_settings():
    ...

def create_config(path, settings):
    ...

def create_vault(path, master_password):
    ...

def setup():
    setup_dialogue()

    storage_path = ask_storage_path()
    master_password = setup_masterpassword()
    settings = ask_settings()

    create_config(storage_path, settings)
    create_vault(storage_path, master_password)

def config_exists():
    ...

def check_setup():
    if not config_exists():
        setup()