# passing function as parameter to other function

def display(fun):
    return "Hello "+fun

def name():
    return "Andy"

print(display(name()))