from collections import deque

class stack:
    def __init__(self,x):
        self.data=deque(x)
        
    def add(self,x):
        self.data.append(x)
        
    def pop(self):
        self.data.pop()
        
    def __repr__(self):
        return "stack([" + ", ".join(repr(item) for item in self.data) + "])"
    
class queue:
    def __init__(self,x):
        self.data=deque(x)
        
    def add(self,x):
        self.data.append(x)
        
    def pop(self):
        self.data.popleft()
        
    def __repr__(self):
        return "queue([" + ", ".join(repr(item) for item in self.data) + "])"