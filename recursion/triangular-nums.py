def triangular_num(n):
    if n > 0:
        return n + triangular_num(n-1)
    else:
        return 0

print(triangular_num(3))