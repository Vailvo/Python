#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
# coverting the bill to a float and storing input as bill variable
tip = int(input("How much would you like to tip? 12%, 15%, 25% ?\n"))
# converting tip variable from input string into an integer(whole number)
total_with_tip = tip / 100 * bill + bill
# dividing tip by 100 to get the decimal value of tip then multiplying by bill for the percentage of tip. Adding the bill to get the total bill amount with tip.

split_bill = int(input("How many people to split the bills?\n"))
# splitting the bill with how many people
final_bill = round(total_with_tip / split_bill, 2)
# final_bill is rounded with the method round, total_with_tip is divided by split_bill(number of people) and the int value of 2 to move the decimal 2 places to the right.
print(f"Each person should pay ${final_bill}.")
# final output ex: $00.00