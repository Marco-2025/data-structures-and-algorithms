def first_index(string):
    if string[0] == "x":
        return 0
    else:
        return 1 + first_index(string[1:])
    
print(first_index("abcdefghijklmnopqrstuvwxyz"))