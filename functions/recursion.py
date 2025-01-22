# Recusion means ; when a function uses itself

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    return result

print(factorial(3))