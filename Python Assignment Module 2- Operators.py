# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:57:02 2021

@author: Ayush
"""

#1.	A. Write an equation which relates   399, 543 and 12345 
#(i)
(399 * 10) + (543 * 10) + 2925 # this will give 12345

#(ii) or
x = 12345
y = 543
z = 399

equation = 22*y + z

if equation == x:
    print('it is a valid relation')
    
#B.  “When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2”—
#How would you justify it.

# this will produce 1 because // results the answer with rounded off  
5//3 

# this will produce (-2) beacuse -1.6 is close to -2 negative number so
# system is rounding of to the lowest negative number
-5 // 3 

###############################################################################

#Problem 2: a=5,b=3,c=10.. What will be the output of the following:
    
a=5
b=3
c=10

# A) a/=b
a = a/b 
print(a)

# B) c*=5      

c= c*5 
print(c) 


############################################################

#Problem 3 A): How to check the presence of an alphabet ‘s’ in word “Data Science” 

#By using Substring for Captial S
string = "Data Science"

substring = "S"

count = string.count(substring)

print("The count is:", count)


#By using Substring for Small S
string = "Data Science"

substring = "s"

count = string.count(substring)

print("The count is:", count)

#Membership Operators
# It will check that left value is a member of right value or not 

"s" in "Data Science" # small alphabet

"S" in "Data Science" # capital alphabet


#B) How can you obtain 64 by using numbers 4 and 3.

x = 4**3 # use 4x4x4 = 64
print(x)

