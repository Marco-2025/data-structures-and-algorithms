
def bubble_sort(array):
    last_index = len(array)-1
    sorted = False
    step_count = 0

    #range will exclude the actual last index
    #the last index is actually not needed because i+1
    #the last pointer index is last_index - 1
    while not sorted:
        sorted = True
        for i in range(last_index):
            #preemptively change to true
            #if no shifts happen then we know the array is sorted in ascending order
            if array[i] > array[i+1]:
                #this is the equivalent of using a temp variable and swapping
                #python does this automatically
                #tuple unpacking
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
                step_count += 1
        last_index -= 1

    return array, step_count

print("Original Array: ", [5,4,3,2,1])
print("Ordered Array: ", bubble_sort([5,4,3,2,1])[0])
print("Steps: ", bubble_sort([5,4,3,2,1])[1])

#Efficiency relevant steps: comparison (if statement) and swapping (variable swap)
#Number of comparisons = Number of swaps
#Number of comparisons * 2 is thus the number of steps
#Worse case scenario is a list ordered in descending order as its the opposite
#Number of steps is approximately N^2 where N is the number of data elements in the array
#Thus, bubble sort's time complexity is approximately O(N^2) AKA Quadratic Time


