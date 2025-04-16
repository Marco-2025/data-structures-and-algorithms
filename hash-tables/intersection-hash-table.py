def intersection_array(array1, array2):
    hash_table = {}
    for a in array1:
        hash_table[a] = True
    
    intersection = []
    for b in array2:
        if hash_table.get(b):
            intersection.append(b)
    return intersection

print(intersection_array([1,2,3,4,5], [0,2,4,6,8]))

#O(N), where A+B = N