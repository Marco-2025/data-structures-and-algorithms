def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array)-1
    steps = 0

    while lower_bound <= upper_bound:
        mid_point = round((upper_bound+lower_bound)/2)
        mid_value = array[mid_point]
        steps += 1
        if mid_value == value:
            return "Steps: " + str(steps) + ", Index: " + str(mid_point)
        elif mid_value < value:
            lower_bound = mid_point + 1
        elif mid_value > value:
            upper_bound = mid_point - 1
    return "Not in array. " + "Steps: " + str(steps)
        
ordered_array = range(1,101)
print(binary_search(ordered_array, 50))