#python Program to find the square root
def square_root(number):
    result = number**0.5

    return result

number = int(input("Enter a number: "))
print("The square root of the number is : ", square_root(number))

#Python program to find the largest Among Three Numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if (a > b and a > c):
    print("a is the largest number")
elif(b > a and b > c):
    print("b is the largest number")
else:
    print(" c is the largest number")

#python Program to solve Quadratic Equation
import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check for real roots
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The roots are real and distinct: {root1:.2f} and {root2:.2f}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"The roots are real and equal: {root:.2f}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The roots are complex: {real_part:.2f} ± {imaginary_part:.2f}i")

# Input coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Check if 'a' is zero
if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    solve_quadratic(a, b, c)


# program to convert celsius to fahrenheit
celsius = float(input())
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius, fahrenheit))

    