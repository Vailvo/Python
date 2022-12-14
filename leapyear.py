year = int(input("What year would you like to check? "))
# modulous % finds the remainder of the operand and by using == 0 to check if there is a remainder
if year % 4 == 0:
    print("Leap Year! 4")
elif year % 100 == 0:
    print("Not a Leap Year. 100")
elif year % 400 == 0:
    print("Leap Year! 400")
else:
    print("Nope")