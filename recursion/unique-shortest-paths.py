def unique_paths(nrow, ncol):
    if nrow == 1  or ncol == 1:
        return 1
    else:
        return unique_paths(nrow-1, ncol) + unique_paths(nrow, ncol-1)


print(unique_paths(7,6))
