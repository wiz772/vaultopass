import os
import json

CONFIG_DIR = os.path.expanduser("~/.vaultopass")

CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")
VAULT_PATH = os.path.join(CONFIG_DIR, "vault.enc")

DEFAULT_TIMEOUT = 30

def get_config_dir_path():
    return CONFIG_DIR

def load_config():
    if not config_exists: return False

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config = json.load(file)
    return config

def write_config(config):
    os.makedirs(CONFIG_DIR, exist_ok=True)

    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)

def create_config(settings):
    timeout = settings

    config = {
        "version": 1,
        "timeout": timeout,
        "vault_path": VAULT_PATH
    }

    write_config(config)
    return config

def config_exists():
    return os.path.isfile(CONFIG_PATH)