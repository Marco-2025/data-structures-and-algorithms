def countdown(num):
    print(num)
    if num > 0:
        countdown(num-1)

countdown(10)

#recursion is simply when a function calls itself
#could have used loop instead
#opt to use recursion if useful or more elegance than a loop