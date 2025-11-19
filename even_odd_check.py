# A python program that checks if a number is odd or even

def check(number):
    result = number % 2
    if result == 0:
        print(f"The {number} is even.")
    else:
        print(f"The {number} is odd.")


check(35)
check(36)
