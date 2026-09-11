class Session:
    def __init__(self, timeout):
        self.unlocked = False
        self.timeout = timeout

    def unlock(self, password):
        if check_password(password):
            self.unlocked = True
            return True

        return False

    def lock(self):
        self.unlocked = False

    def is_unlocked(self):
        return self.unlocked


def check_password(test_password):  
    hashed_test_password = test_password
    real_password = "aaa"
    return hashed_test_password == real_password