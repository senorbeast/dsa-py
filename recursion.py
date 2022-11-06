###### Recursion

# Base Case
# Nested function


#### Factorial

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

for i in range(1,20):
    print(factorial(i))


## Time Complexity
# n! -> n multiplications steps -> 
# O(n)

## Space Complexity
# O(n)   
# Function will wait till the all the nested functions outputs are received, this takes space (the variable and function) 



#### Fibonaaci

def fibonaaci(n):
    if n <= 1:
        return 1
    return fibonaaci(n-1) + fibonaaci(n-2)

for i in range(20):
    print(fibonaaci(i))
    

# We have 2 branches in the recursive tree
# fibonaaci(5)
# fib4 + fib 3
# fib 3 + fib2 , fib(2) + fib(1)
# fib 2 + fib1 , fib1 fib0, fib1 fib0 , fib(1)
# fib1 fib 0, fib1, fib1 fib0, fib1 fib0 fib1


# Height of the tree with be roughly n
# No. of calcs: 2^n 
# No. of ops in 1 calc: 1
# 2^n is dominated by 2^n the term. 
# O(2^n)


# Since, 2^(n+1) = 2^(n) = 2^(n-1), For Complexity, since we don't care about constants with n