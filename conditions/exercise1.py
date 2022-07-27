# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if the number variable is divisible by 2 it should have a remainder of 0 thus the == to check precisely.
if number % 2 == 0:
  print(f" The number {number} is even!")
  # if the remainder is not equal to 0 than the number is odd and the else statement is executed.
else:
  print(f"The number {number} is odd!")