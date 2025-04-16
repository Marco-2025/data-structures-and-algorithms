def even_numbers(arr):
    if len(arr) > 1:
        if arr[len(arr)-1] % 2 != 0:
            arr.pop()
            return even_numbers(arr)
        elif len(arr) > 2:
            return [arr[len(arr)-1]] + even_numbers(arr[:len(arr)-1])
        else:
            return [arr[1]]

print(even_numbers([1,2,3,4,5,6]))