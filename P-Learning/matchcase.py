# A cool program to understand the match case concept in python

month = input("Enter any month of a year (January - December): ")
month = month.lower()

match month:
    case "january":
        print("We are in the first month of the year.")
    case "february":
        print("We are in the second month of the year.")
    case "march":
        print("We are in the third month of the year.")
    case "april":
        print("We are in the fourth month of the year.")
    case "may":
        print("We are in the fifth month of the year.")
    case "june":
        print("We are in the sixth month of the year.")
    case "july":
        print("We are in the seventh month of the year.")
    case "august":
        print("We are in the eighth month of the year.")
    case "september":
        print("We are in the ninth month of the year.")
    case "october":
        print("We are in the tenth month of the year.")
    case "november":
        print("We are in the eleventh month of the year.")
    case "december":
        print("We are in the last month of the year.")
    case _:
        print("The world doesn't know the kind of month you typed.")
