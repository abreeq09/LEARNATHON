#Getting Started With day-2
#Escape Sequence
#by using /:  
string = "Hi!\"man"
print (string)  

#by using \n:
string = "Hi\nman"
print(string)

#by using \t:
string = "Hi\tman"
print(string)

#by using \r:
string = "Hi\rman"
print(string)

#by using \b:
string = "Hi\bman"
print(string)

#\ooo Represents Octal number in the string
string = "\543\432\789"  
print (string)  

#xhh Represents hexadecimal representations of the string
string = "\x54\x34"  
print (string)  

#Operators

#Arithmetic Operators
a = 10
b = 15

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)   

#Assignment Operators
# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b      # a = a + b

print(a)

#Comparison Operator
a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

#Logical Operator
x = 5
y = 10

# AND operator
if x > 0 and y < 15:
    print("Both conditions are true")

# OR operator
if x > 10 or y < 5:
    print("At least one condition is true")

# NOT operator
if not x == y:
    print("x is not equal to y")

#Bitwise Operators
#AND
a = 7
b = 4

# Print bitwise AND operation
print("a & b =", a & b)

#OR
a = 7
b = 4

# Print bitwise OR operation
print("a | b =", a | b)

#XOR
a = 7
b = 4

# print bitwise XOR operation
print("a ^ b =", a ^ b)

#NOT
a = 7
b = 4

# Print bitwise NOT operation
print("~a =", ~a)

#Bitwise Right shift
a = 10
b = -10

# print bitwise right shift operator
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

#Bitwise Left Shift
a = 5
b = -10

# print bitwise left shift operator
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)

#Specail Operator
#Identity Operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  #prints false

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False because lists are equal but not  identical

#Memebership Operator
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False

#User Input & Variables
#Assigning value to Variables
name = 'Designer'
print(name)

#changing the value of a Variable
name = 'Designer'
print(name)

#new value Assigning
name = 'Developer'
print(name)

#Assigning multiple values to multiple variables
name, designation, hobby = 'Abreeq', 'Designer', 'crafts'
print(name)
print(designation)
print(hobby)

#Literals
#literals are nothing but values assigned to variables
#there are 4 types of literals
#1. Integer
#2.Floating
#3.Complex
#4.String

#Data Types
num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))

#Access List items
languages = ["Swift", "Java", "Python"]

# access element at index 0
print(languages[0])  

# access element at index 2
print(languages[2])  

#access Tuple items
# create a tuple 
product = ('Microsoft', 'Xbox', 499.99)

# access element at index 0
print(product[0])   

# access element at index 1
print(product[1])  

#String Data Type
name = 'learnathon'
print(name)  

message = 'python for beginners'
print(message)

#Set Data Type
# create a set named student_id
student_id = {112, 114, 116, 118, 115}

# display student_id elements
print(student_id)

# display type of student_id
print(type(student_id))


#Dictonary Data Type
# create a dictionary named capital_city
capital_city = {'India': 'Hyderabad', 'Italy': 'Rome', 'England': 'London'}
print(capital_city)

#Access dictionary values
# create a dictionary named capital_city
capital_city = {'India': 'Hyderabad', 'Italy': 'Rome', 'England': 'London'}

print(capital_city['India'])  # prints Hyderabad

# write a program that prints a formatted message using escape Characters
print("newline Character\n"
    "Tab character\t"
      "\"escape\"character\"\n")

#Program to calculate the total cost of items including tax
num_items = int(input("Enter no of items:"))
cost_per_item = float(input("Enter the cost of item:"))

total_cost_before_tax = num_items * cost_per_item

tax = 0.5
tax_amount = total_cost_before_tax * tax

total_cost_after_tax = tax_amount * total_cost_before_tax

print("Total cost before tax: ${:.2f}".format(total_cost_before_tax))
print("Tax: ${:.2f}".format(tax))
print("Total cost after tax: ${:.2f}".format(total_cost_after_tax))

#Program to calculate area of rectangle
length = float(input("enterlength:"))
width = float(input("enter width:"))

area = length * width
print("Area of the rectangle: {:.2f} sq".format(area))

#Program to swap the variables
a = 100
b = 200

a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)