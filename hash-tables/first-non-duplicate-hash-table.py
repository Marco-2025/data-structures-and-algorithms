def first_non_duplicate(str):
    hash_table = {}
    for i in str.replace(" ", ""):
        if hash_table.get(i) != None:
            hash_table[i] += 1
        else:
            hash_table[i] = 1

    for a in str.replace(" ", ""):
        if hash_table.get(a) == 1:
            return a
    return 0
print(first_non_duplicate("minimum"))

#str*2 the efficiency is 2N thus O(N)