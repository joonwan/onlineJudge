def factorial(n):
    
    if n <= 1:
        return 1
    
    return n*factorial(n-1)

test = factorial(0)
print(test)