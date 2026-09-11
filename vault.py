from session import Session

def open_vault(session):
    if not session.is_unlocked():
        if not session.unlock():
            print("Failed to unlock your session. Your vault is still sealed.")
            return

    # session unlock, vault unsealed
    print("ok déverouillé.") 