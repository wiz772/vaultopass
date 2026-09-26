from core.session import Session
import utils.utils as utils

def open_vault(session):
    if not session.is_unlocked():
        if not session.unlock():
            print("Failed to unlock your session. Your vault is still sealed.")
            return

    # session unlock, vault unsealed
    utils.setting_window_name("VaultoPASS - Vault")
    print("ok déverouillé.") 


def update_vault(session, data):
    ...