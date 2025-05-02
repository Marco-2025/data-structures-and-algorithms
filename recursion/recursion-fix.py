def add_until_100(array):
    if not array:
        return 0
    
    sum_of_the_rest = add_until_100(array[1:])

    if array[0] + sum_of_the_rest > 100:
        return sum_of_the_rest
    else:
        return array[0] + sum_of_the_rest
    
print(add_until_100([1,2,3]))

#two paths to improve: memoization or iteration/bottom-up, or store in a var

#creating the var was the best option