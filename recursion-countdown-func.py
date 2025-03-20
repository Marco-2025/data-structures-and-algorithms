def countdown(num):
    if num > -1:
        print(num)
        countdown(num-1)

countdown(10)

#recursion is simply when a function calls itself
#could have used loop instead
#opt to use recursion if useful or more elegance than a loop