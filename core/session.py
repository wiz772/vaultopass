from vault import vault_handler
from cryptography.exceptions import InvalidTag

class Session:
    def __init__(self, timeout):
        self.unlocked = False
        self.timeout = timeout
        self.vault_data = None
        self.encryption_key = None

    def unlock(self, password):
        try:
            vault_data, encryption_key = vault_handler.decrypt_vault(password)

            self.vault_data = vault_data
            self.encryption_key = encryption_key
            self.unlocked = True

            return True

        except InvalidTag:
            return False
    
    def lock(self):
        self.vault_data = None
        self.encryption_key = None
        self.unlocked = False

    def is_unlocked(self):
        return self.unlocked