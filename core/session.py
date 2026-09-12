class Session:
    def __init__(self, timeout):
        self.unlocked = False
        self.timeout = timeout

    def unlock(self, password):
        self.unlocked = True
        return True
    
    def lock(self):
        self.unlocked = False

    def is_unlocked(self):
        return self.unlocked
