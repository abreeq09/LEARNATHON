#KEYWORDS
#Keywords are predefined, reserved words used in Python programming that have special meanings to the compiler.
#All the keywords except True, False and None are in lowercase and they must be written as they are. The list of all the keywords is given below.
#To check keywords
import keyword
print(len(keyword.kwlist))

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
#'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
#'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#TYPE CONVERSIONS
#1. Implicit Conversion- Python automatically converts one data type to another.
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

#Explicit Type Conversion-We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

#STRINGS
#Access string
greet = 'hello'

# access 1st index element
print(greet[1]) # "e"

greet = 'hello'

# access 4th last element
print(greet[-4]) # "e"

#Multiline string
# multiline string 
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)

#String Operations
str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)

 #Join Two or more strings
greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)

#Iterate through string
greet = 'Hello'

# iterating through greet string
for letter in greet:
    print(letter)

# Program to Concatenate Strings
str1 = input("enter string1")
str2 = input("enter string2")
concat = str1 + str2
print("concatenated string: ",concat)

#program to find length of a string
string = "Abreeq"
print(len(string))

#Program to Reverse a string
string = input("enter string:")
reversed_string = string[::-1]
print("reversed string:", reversed_string)

#program to convert string to uppercase
string = input("enter string:")
uppercase = string.upper()
print("Uppercase string:", uppercase)
