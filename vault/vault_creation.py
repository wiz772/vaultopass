from crypto import crypto
from utils import config
import os
import json

def save_encrypted_vault(data, nonce):    
    config_dir = config.get_config_dir_path()
    vault_path = os.path.join(config_dir, "vault.enc")
    
    with open(vault_path, "wb") as file:
        file.write(nonce)
        file.write(data)


def save_meta_data(data):
    config_dir = config.get_config_dir_path()
    meta_path = os.path.join(config_dir, "vault_meta.json")

    with open(meta_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def new_empty_vault():
    vault_structure = {
        "entries": []
    }
    return vault_structure

def new_vault_metadata_structure(salt):
    metadata_structure = {
        "kdf": {
            "algorithm": crypto.KDF_ALGORITHM,
            "salt": salt.hex(),
            "time_cost": crypto.KDF_TIME_COST,
            "memory_cost": crypto.KDF_MEMORY_COST,
            "parallelism": crypto.KDF_PARALLELISM,
            "hash_len": crypto.KDF_HASH_LEN
        }
    }
    return metadata_structure


def create_vault(master_password):
    salt = crypto.generate_salt()
    encryption_key = crypto.derive_key(master_password, salt)

    vault_data = new_empty_vault()
    plaintext = json.dumps(vault_data).encode("utf-8")
    encrypted_data, nonce = crypto.encrypt(plaintext, encryption_key)


    vault_metadata = new_vault_metadata_structure(salt)

    save_encrypted_vault(encrypted_data, nonce)
    save_meta_data(vault_metadata)