class Session:
    def __init__(self, timeout):
        self.unlocked = False
        self.timeout = timeout

    def unlock(self):
        passw = input("Enter your password: ")
        if passw == "aaa":
            self.unlocked = True
            return True
        return False
    
    def lock(self):
        self.unlocked = False

    def is_unlocked(self):
        return self.unlocked