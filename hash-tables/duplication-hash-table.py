def first_duplicate(array):
    hash_table = {}
    for a in array:
        hash_table[a] = True
    
    hash_table_2 = {}
    for b in array:
        if hash_table_2.get(b) == None:
            hash_table_2[b] = 0

        if hash_table.get(b):
            hash_table_2[b] += 1

        if hash_table_2.get(b) > 1:
            return b
    
    return None

print(first_duplicate(['a', 'b', 'c', 'd', 'c', 'e', 'e']))

#O(N) because the efficiency is approximately 2N + 3 but the constants are dropped.