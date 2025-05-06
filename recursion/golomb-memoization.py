def golomb(n, obj):
    if n == 1:
        return 1
    
    if n not in obj:
        obj[n] = 1 + golomb(n - golomb(golomb(n-1, obj), obj), obj)
    
    return obj[n]


print(golomb(10, {}))