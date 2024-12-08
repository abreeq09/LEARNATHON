#if elif else
#Write a program that checks if a given number is positive, negative, or zero. If it's positive, print "Positive number." If it's negative, print "Negative number." If it's zero, print "Zero."
a = int(input("enter a number: "))
if a >= 1:
    print("a is positive")
elif a <= -1:
    print("a is negetive")
else:
    print("it is zero")

#Create a program that takes a student's exam score as input. Classify the student's performance as follows:
# - If the score is greater than or equal to 90, print "A"
# - If the score is between 80 and 89, print "B"
# - If the score is between 70 and 79, print "C"
# - If the score is between 50 and 69, print "D"
# - If the score is below 50, print "F"
marks = float(input("enter marks: "))    
if marks >= 90:
    print("A")
elif  80 < marks < 89:
    print("B")
elif  70 < marks < 79:
    print("C")
elif  50 < marks < 69:
    print("D")
elif  marks < 50:
    print("F")
else:
    print("Not defined")

#> Write a program that determines whether a given year is a leap year or not. A leap year is either divisible by 4 but not divisible by 100, or it is divisible by 400.
year = int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is leap year.".format(year))
else:
    print(f"{year} is not leap year.".format(year))

#Write a Python program that determines the price of a movie ticket based on the age and time of the show. The program should take the age and time (in 24-hour format) as inputs and use the **`match`** statement to calculate and print the ticket price according to the following rules:

#- For age 0-5, the ticket is free.
#- For age 6-12, the ticket is $10.
#- For age 13-18, the ticket is $15.
#- For age 19 and above, the ticket is $20.
#- For shows before 12:00 PM, there is a $5 discount on the ticket.
    
age = int(input("enter age: "))
time = int(input("enter time: "))

match age:
    case 0|1|2|3|4|5:
        ticket_price = 0
    case 6|7|8|9|10|11|12:
        ticket_price = 10
    case 13|14|15|16|17|18:
        ticket_price = 15
    case _:
        ticket_price = 20

if time < 12:
        ticket_price -= 5
print(f"The price is ${ticket_price}",ticket_price)

        