#Data Types
#String

print("Hello"[0])
print("Hello"[4])

#Integers

print(48484 + 892034)

#Float

3.1476

#boolean

True
False

#This method will tell you what data type
ten = 10
print(type(ten))

#Type conversion or Type casting -- where a data type is changed into a different data type

new_ten = str(ten)
print(type(new_ten))

#len() does not like ints
len(2333)
#error 
#Cannot concatenate strings with ints
num_char =len(input("What is your name?"))
print("Your name has" + num_char + " characters.")

#TypeError: can only concatenate str(not"int") to str

#To fix the TepeError you can convert num_char into a str

new_num = str(num_char)

#Then use a new print()

print("Your name has" + new_num + " characters.")

print(70 + float("100.5"))

#output 170.5
#"100.5" is a string that gets converted into a float