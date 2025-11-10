# A simple python program to check elegibility of voters.

age = int(input("Enter your age: "))

match age:
    case 18 | 19: # matching multiple values with pipe (|)
        if age >= 18 and has_id(user): 
            # TODO: remember to write the function - has_id.
            print("You are eligible to vote in this election.")
        else:
            print("You need a valid ID to vote.")
    case _:
        print("You are not eligible to vote.")
