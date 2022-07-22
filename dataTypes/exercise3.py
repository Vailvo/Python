# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# converting age into a integer
# storing the conversion as new_age variable
new_age = int(age)
# x is equal to 90
x = 90 - new_age
# multiple x with how many days in a year
days = x * 365 
# multiple x with how many weeks in a year
w = x * 52
# multiple x with how many months in a year
m = x * 12

print(f"You have {days} days, {w} weeks, and {m} months left.")

# To caculate how many days, weeks, and months left before turning 90 years old