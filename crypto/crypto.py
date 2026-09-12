import secrets
from argon2.low_level import hash_secret_raw, Type

def generate_salt():
    salt = secrets.token_bytes(16)
    return salt

def derive_key(password, salt):
    key = hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32,
        type=Type.ID,
    )
    return key