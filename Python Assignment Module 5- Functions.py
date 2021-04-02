# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:57:02 2021

@author: Ayush
"""

# Q1. A) Find the magnitude of (3+5j)
   # B) list1 = [1,5.5, (10+20j),’data science’].. Print default functions and parameters exists in list1.
   # C) How do we create a sequence of numbers in Python.
   # D) Read the input from keyboard and print a sequence of numbers up to that number. '''

# A.
import numpy as np
vector=np.array([3,4])
magnitude=np.linalg.norm(vector)
print(magnitude)

# B. 
list1 = [1,5.5, (10+20j),"data science"]
list1.append(20)
print(list1)

# C.      
numbers=range(1,10)
sequence_of_numbers=[]
for number in numbers :
    if number % 5 in (1,2):
        sequence_of_numbers.append(number)
        print(sequence_of_numbers)
        
# D.
import numpy as np
a = int(input("Enter a number: "))
print(np.arange(a))

###############################################################################
 #  Q2. Write a simple user defined function that greets a person in such a way that:
    #  i) It should accept both name of person and message you want to deliver.
    #  ii) If no message is provided, it should greet a default message ‘How are you’
    #  Ex: Hello ---xxxx---, How are you - default message.
    #  Ex: Hello ---xxxx---, --xx your message xx---
    

name = input("Enter the name: ")
msg = input("Enter the message: ")
if msg == "":                       #In-case of No personal message
    print("Hello " + name + ". " + "How are you ?")
else:                               #In-case of personal message
    print("Hello " + name + ". " + msg)

###############################################################################
 #  Q3.By using a filter function, find positive number present in a list.
    #       Lsit1= [2, 6, -5, 4, -8, -9, 10, 1]

#By using a filter function, find positive number present in a list
nums=[2, 6, -5,4,-8,-9,10,1]
print("original numbers in the list:",nums)
new_nums=list(filter(lambda x: x>0,nums))
print("positive numbers in the list:", new_nums)

###############################################################################