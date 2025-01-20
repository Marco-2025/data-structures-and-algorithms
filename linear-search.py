def linear_search(array, value):
    for index, item in enumerate(array):
        if value == item:
            return "steps: " + str(index+1)
        elif value < item:     
            return "steps: " + str(index+1)
        elif index == len(array)-1:
            return "steps: " + str(len(array))

ordered_array = [1,2,3,4,5]
print(linear_search(ordered_array, 5))