import secrets
from argon2.low_level import hash_secret_raw, Type

KDF_ALGORITHM = "argon2id"
KDF_TIME_COST = 3
KDF_MEMORY_COST = 65536
KDF_PARALLELISM = 4
KDF_HASH_LEN = 32

def generate_salt():
    salt = secrets.token_bytes(16)
    return salt

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