import string
def missing_letter_finder(str):
    hash_table = {}

    for i in str.replace(" ", ""):
        hash_table[i] = True

    for a in string.ascii_lowercase:
        if hash_table.get(a) == None:
            return a
        
print(missing_letter_finder("the quick brown box jumps over a lazy dog"))

# alphabet length = M, input str = N, efficiency is 2M+N, thus O(N)