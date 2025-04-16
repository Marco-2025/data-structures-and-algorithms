def linear_search(array, value):
    for index, item in enumerate(array):
        if value == item:
            return "steps: " + str(index+1)
        elif value < item:     
            return "steps: " + str(index+1)
        elif index == len(array)-1:
            return "steps: " + str(len(array))

ordered_array = range(1,101)
print(linear_search(ordered_array, 76))
#76 Steps to find 76
#O(N) Linear Time: The amount of steps taken by the algorithm are proportional to the amount of data elements
