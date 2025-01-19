def linear_search(array, value):
    for index, item in enumerate(array):
        if value == item:
            print("steps:", index+1)
            return value
        elif value < item:
            print("steps:", index+1)
            break

ordered_array = [1,2,3,4,5]
print(linear_search(ordered_array, 3.3))