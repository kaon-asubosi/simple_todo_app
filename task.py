class Task:
    def __init__(self, name:str,minutes:int,done=False):
        self.name = name
        self.minutes = minutes
        self.done = done
    
    def __repr__(self):
        return f"{"[✓]" if self.done else "[ ]"} {self.name} - {self.minutes}分"
    
    def __clear__(self):
        self.done = not(self.done)