# A python program that sums up any number given to a function

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
