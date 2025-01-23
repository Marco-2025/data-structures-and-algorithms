def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array)-1
    steps = 0

    while lower_bound <= upper_bound:
        #floored division // instead of / which is regular float division
        mid_point = (upper_bound+lower_bound)//2
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
print(binary_search(ordered_array, 76))
#2 Steps to find 76
#O(log N) Log Time: The algorithm takes as many steps as it takes to halve the
#amount of data elements until reaching 1. I.e Log2(8) = 3