# Rollercoaster ride
# if / elif / else
height = int(input("What is your height? (cm) "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
# if the age is less than 12 or 12, the payment is $5
    if age < 12:
        print("Please pay $5.")
# if the age is less than 18 and older then 12. the payment is $7
    elif age <= 18:
        print("Please pay $7.")
# if the age is older than 18, the payment is $12
    else:
        print("Please pay $12")
else:
    print("Sorry, you're not tall enough to ride the rollercoaster.")