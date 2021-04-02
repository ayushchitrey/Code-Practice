# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:57:02 2021

@author: Ayush
"""

# Q1.	 Take a variable age which is of positive value and check the following:
    #a. If age is less than 1, print 'infant'
    #b. If age is between 1 to 14, print 'child'
    #c. If age is between 15 to 60, print 'Adult'
    #b.	If age is more than 60, print ‘senior citizens’
    
age=int(input("Enter Age : "))
if age<1:
    print("INFANT")
elif age>=1 and age<=14:
    print("CHILD")
elif age>=15 and age<60:
    print("ADULT")
elif age>=60:
    print("SENIOR CITIZEN")
else:
    print("check that your input is an integer and try again")

###############################################################################
 #Q2.	Find the final train ticket price with the following conditions. 
  # a.	If male and senior citizen, 70% of fare is applicable
   # b.	If female and senior citizen, 50% of fare is applicable.
   # c.	If female and normal citizen, 70% of fare is applicable
    #d.	If male and normal citizen, 100% of fare is applicable
    #[Hint: First check for the gender, then calculate the fare based on age factor.
     #For both Male and Female, consider them as senior citizens if their age >=60] 

gender=str(input("Enter Gender: "))
if gender=="male":
    age=int(input("Enter Age : "))
    if age<60:
        print("Normal Citizen - 100% of fare is applicable")
    elif age>=60:
        print("Senior Citizen - 70% of fare is applicable")
    else:
        print("check that your input is an integer and try again")
        
elif gender=="female":
    age=int(input("Enter Age : "))
    if age<60:
        print("Normal Citizen - 70% of fare is applicable")
    elif age>=60:
        print("Senior Citizen - 50% of fare is applicable")
    else:
        print("check that your input is an integer and try again")
    
###############################################################################
# Q3.	Check whether the given number is positive and divisible by 5 or not.

number = float(input("Enter a number: "))
if number > 0:
   print("Positive number")
   if(number % 5 == 0):
       print("Given Number {0} is Divisible by 5".format(number))
   else:
       print("Given Number {0} is Not Divisible by 5".format(number))
       
elif number == 0:
   print("Zero")
   if(number % 5 == 0):
       print("Given Number {0} is Divisible by 5".format(number))
   else:
       print("Given Number {0} is Not Divisible by 5".format(number))
       
else:
   print("Negative number")
   if(number % 5 == 0):
       print("Given Number {0} is Divisible by 5".format(number))
   else:
       print("Given Number {0} is Not Divisible by 5".format(number))

############################################################################### 
