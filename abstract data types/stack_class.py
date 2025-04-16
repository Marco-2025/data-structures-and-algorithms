class Stack:
    def __init__(self):
        self.underlying_array = []
    
    def push(self, data):
        self.underlying_array.append(data)
    
    def read(self):
        if len(self.underlying_array) > 0:
            return self.underlying_array[len(self.underlying_array)-1]
        else:
            return None
    def pop(self):
       return self.underlying_array.pop()