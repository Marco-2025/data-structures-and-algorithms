def unique_paths(rows, columns, obj):
    if rows == 1 or columns == 1:
        return 1
    elif str(sorted((rows,columns))) not in obj:
        obj[str(sorted((rows,columns)))] = unique_paths(rows-1,columns, obj) + unique_paths(rows,columns-1, obj)
    
    return obj[str(sorted((rows,columns)))]

print(unique_paths(5, 5, {}))