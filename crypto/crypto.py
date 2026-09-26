import secrets
from argon2.low_level import hash_secret_raw, Type
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KDF_ALGORITHM = "argon2id"
KDF_TIME_COST = 3
KDF_MEMORY_COST = 65536
KDF_PARALLELISM = 4
KDF_HASH_LEN = 32

AES_GCM_NONCE_SIZE = 12
AES_GCM_BIT_SIZE = 256
AES_GCM_TAG_SIZE = 16

def generate_salt():
    salt = secrets.token_bytes(16)
    return salt

def generate_aes_gcm_nonce():
    nonce = secrets.token_bytes(AES_GCM_NONCE_SIZE)
    return nonce

def derive_key(password, salt):
    key = hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=KDF_TIME_COST,
        memory_cost=KDF_MEMORY_COST,
        parallelism=KDF_PARALLELISM,
        hash_len=KDF_HASH_LEN,
        type=Type.ID,
    )
    return key



def encrypt(data, key):
    aesgcm = AESGCM(key)
    nonce = generate_aes_gcm_nonce()

    encrypted_data = aesgcm.encrypt(nonce, data, None)

    return encrypted_data, nonce

def decrypt(encrypted_data, key, nonce):
    aesgcm = AESGCM(key)
    decrypted_data = aesgcm.decrypt(nonce, encrypted_data, None)

    return decrypted_data