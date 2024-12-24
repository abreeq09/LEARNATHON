#Write a Python program to get the largest number from a list
s = [2,3,4,5,10,8]
large = s[0]
for i in s:
    if i > large:
        large = i
print("lagest number : ",large)


#Write a Python program to clone or copy a list
alist = [10,20,30,40]
old_list = alist.copy()
print(old_list)


#Write a Python program to find the repeated items of a tuple
def repeated_items(input_tuple):
    repeated = set([item for item in input_tuple if input_tuple.count(item) > 1])
    return repeated

input_tuple = (1,3,2,4,5,3,5,3,5)
result = repeated_items(input_tuple)
print("Repeated items:",result)

#method 2
s = (2,4,4,5,2,7)
count = s.count(4)
print(count)
