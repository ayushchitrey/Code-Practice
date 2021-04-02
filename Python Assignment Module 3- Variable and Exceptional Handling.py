# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:26:07 2021

@author: Ayush
"""

#Problem 1:	What will be the output of the following (can/cannot):
#a)
Age1=5
print(Age1)
type(Age1)  

#b) 
    5age=55 #Its not valid as Variable name should start with letter only

############################################################################

#Problem 2:	What will be the output of following (can/cannot):

#a)

Age_1=100
print(Age_1)
type(Age_1)

#b)
age@1=100  #Its not valid as Variable name, It can contain alphanumerics and
           # underscore only special character not allowed
#########################################################################

#Problem 3)	How can you delete variables in Python ?

Number = 45
Number

#delete variable
del (Number)
Number   # encounter error after deleteing the Number variable as 
         #"name 'Number' is not defined"
