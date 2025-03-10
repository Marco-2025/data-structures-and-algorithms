import string
def missing_letter_finder(str):
    hash_table = {}
    for letter in string.ascii_lowercase:
        hash_table[letter] = False

    for i in str.replace(" ", ""):
        if hash_table.get(i) != None:
            hash_table[i] = True

    for a in string.ascii_lowercase:
        if hash_table.get(a) == False:
            return a
        
print(missing_letter_finder("the quick brown box jumps over a lazy dog"))

# alphabet length = M, input str = N, efficiency is 2M+N, thus O(N)