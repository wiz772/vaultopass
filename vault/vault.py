from core import session
from utils import utils
from utils import config
from crypto import crypto
import os
import json

def get_vault_meta_data():
    config_dir = config.get_config_dir_path()
    meta_path = os.path.join(config_dir, "vault_meta.json")

    with open(meta_path, "r", encoding="utf-8") as file:
        metadata = json.load(file)

    return metadata

def get_encrypted_vault():
    config_dir = config.get_config_dir_path()
    vault_path = os.path.join(config_dir, "vault.enc")

    with open(vault_path, "rb") as file:
        nonce = file.read(crypto.AES_GCM_NONCE_SIZE)  
        encrypted_data = file.read() 

    return encrypted_data, nonce


def decrypt_vault(master_password):
    metadata = get_vault_meta_data()
    salt = bytes.fromhex(metadata["kdf"]["salt"])
    encryption_key = crypto.derive_key(master_password, salt)

    encrypted_data, nonce = get_encrypted_vault()
    decrypted_data = crypto.decrypt(encrypted_data, encryption_key, nonce)

    vault_data = json.loads(decrypted_data.decode("utf-8"))
    return vault_data

def encrypt_vault(vault_data, encryption_key):
    plaintext = json.dumps(vault_data).encode("utf-8")
    encrypted_data, nonce = crypto.encrypt(plaintext, encryption_key)

    return encrypted_data, nonce

def open_vault(session):
    if not session.is_unlocked():
        if not session.unlock():
            print("Failed to unlock your session. Your vault is still sealed.")
            return

    utils.setting_window_name("VaultoPASS - Vault")
    print("ok déverouillé.") 

def update_vault(session, data):
    ...