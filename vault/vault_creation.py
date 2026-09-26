from crypto import crypto

def save_encrypted_vault(data):
    ...

def save_meta_data(data):
    ...

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
    encrypted_vault = crypto.encrypt(vault_data, encryption_key)

    vault_metadata = new_vault_metadata_structure(salt)

    save_encrypted_vault(encrypted_vault)
    save_meta_data(vault_metadata)