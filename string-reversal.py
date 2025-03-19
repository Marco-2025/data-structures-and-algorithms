from stack_class import Stack

def string_reversor(str):
    string_stack = Stack()
    reversed_string = ""
    for i in str:
        string_stack.push(i) 
        
    while string_stack.read():
        reversed_string += string_stack.pop()

    return reversed_string

print(string_reversor("testing"))

#N*2 is O(N) efficiency