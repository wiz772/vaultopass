from utils import config

def show_settings_menu():
    settings = config.load_config()
    version = settings["version"]
    timeout = settings["timeout"]
    print(f"""
Settings:

Timeout session (minutes): {timeout}

""")