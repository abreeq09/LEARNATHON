#String Slicing
#Syntax for Slicing
#str_object[start_pos:end_pos:step]
s = 'Alinaabreeq'
first_five = s[:5]
print(first_five)

last_five = s[5:11]
print(last_five)

#Reverse string 
s = 'AlinaAbreeq'
reverse = s[::-1]
print(reverse)

#Program that takes a sentence as input and extracts the substring between 5th and 10th characters. Print the extracted substring.
sentence = input("Enter a sentence: ")
if len(sentence) >= 10:
    extracted_substring = sentence[4:10]
    print("extracted substring:",extracted_substring)
else:
    print("Input sentence should have atlest 10 characters")

#PROGRAM TO REVERSE A STRING
string = "alina"
reversed_string = string[::-1]
print("reversed string is: ",reversed_string)

# Write a program to check for alpha numeric characters
#Hint: use `isalnum()`
string = "abreeq09"
alphanumeric = string.isalnum()
print("it is alphanumeric:",alphanumeric)

#Write a program to find how many times abra has occurred in the string ‘abracadabracobra’
#Hint: use count()
string = "abracadabracobra"
count = string.count('abra')
print("count:",count)