import unittest
def leafYear(x):
    if x%4 == 0:
        if x%100 == 0:
            if x%400 == 0:
                print("It's a leap year")
            else:
                print("It's not a leap year")
        else:
            print("It's a leap year")
    else:
        print("It's not a leap year")

