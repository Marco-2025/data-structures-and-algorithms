def string_counter(arr):
    if len(arr) > 1:
        return len(arr.pop()) + string_counter(arr)
    else:
        return len(arr[0])


print(string_counter(["ab", "c", "def", "ghij"]))