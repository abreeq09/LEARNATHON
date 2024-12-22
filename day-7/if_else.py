#program that calculates the factorial of a given number using a for loop.
def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1  # 0! is 1 by definition
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Input from the user
num = int(input("Enter a number to calculate its factorial: "))
result = calculate_factorial(num)
print(f"The factorial of {num} is: {result}")



# write a program that takes a number as input from the user and prints its multiplication table upto 10.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")



# Write a program that takes a number as input from the user and prints its multiplication table up to 10.
num = int(input("enter num: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")   



#Write a program that prints the following pattern using nested loops
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
    

#Create a program to calculate the sum of even numbers from 1 to 50 using a while loop.
start = 1
end = 50
sum_even = 0

while start <= end:
    if start % 2 == 0:
        sum_even += start
    start += 1
print("sum from 1 to 50 even numbers is: ", sum_even)
