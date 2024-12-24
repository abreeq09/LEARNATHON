#Write a recursive function to find the sum of digits of a positive integer.
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
    
num = int(input("Enter number: "))
result = sum_of_digits(num)
print(f"The sum of digits of {num} is {result}")



#Write a recursive function to reverse a string.
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse(s[:-1])
    
string = input("Enter String: ")
result = reverse(string)
print(f"reversed string is {result}")    

    

#write a recursive function to calculate the power of a number (e.g., x^n)?
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

base = float(input("Enter the base (x): "))
exponent = int(input("Enter the exponent (n): "))
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")

