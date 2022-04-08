# Converting a number to a list of integers.

# Source: https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/

# conversion of number to list of integers
# using list comprehension
  
# initializing number 
num = 2019
  
# printing number 
print ("The original number is " + str(num))
  
# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(num)]
  
# printing result 
print ("The list from number is " + str(res))

# ---

# conversion of number to list of integers
# using map()
  
# initializing number 
num = 2019
  
# printing number 
print ("The original number is " + str(num))
  
# using map()
# to convert number to list of integers
res = list(map(int, str(num)))
  
# printing result 
print ("The list from number is " + str(res))