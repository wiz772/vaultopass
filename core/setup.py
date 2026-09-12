def ask_masterpassword():
    ...

def setup_dialogue():
    ...

def ask_storage_path():
    ...

def ask_settings():
    ...

def create_config(path, settings):
    ...

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
    ...

def check_setup():
    if not config_exists():
        setup()