#Write a function called sum_numbers that takes two numbers as arguments and returns their sum.
def sum_numbers(num1, num2):
   return num1 + num2
result = sum_numbers(10, 30)
print(f"Sum: {result}")



#Create a function called grade_converter that takes a numerical grade as an argument and returns the corresponding letter grade (A, B, C, D, F) based on the standard grading scale.
def grade_converter(numerical_grade):
   if numerical_grade >= 90:
      return 'A'
   elif 80 <= numerical_grade <= 89:
      return 'B'
   elif 70 <= numerical_grade <= 79:
      return 'C'
   elif 50 <= numerical_grade <= 69:
      return 'D'
   else:
      return 'F'
grade = grade_converter(85)
print(f"Letter Grade: {grade}")


#Write a Python program that defines a function called outer_function. Inside outer_function, declare a variable x with a value of 10. Then, define another function called inner_function inside outer_function. Inside inner_function, declare a variable y with a value of 5. Return the sum of x and y from inner_function. Finally, call outer_function and print the result.
def outer_function():
   x = 10

   def inner_function():
      y = 5
      return x + y
   result = inner_function()
   return result

result_value = outer_function()
print(f"Result: {result_value}")
