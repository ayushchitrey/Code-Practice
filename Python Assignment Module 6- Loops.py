# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:57:02 2021

@author: Ayush
"""
# Q1.	Print the Palindromes (reverse of the number is itself) that are present in between 100 and 250.
   # (Ex: 121,131,212,222... etc.) 

minimum = int(input("please enter the minimum value:"))
maximum = int(input("please enter the maximum value:"))
print("palindrom Numbers between %d and %d are:"%(minimum,maximum))
for num in range (minimum,maximum+1):
    temp=num
    reverse=0
    while(temp>0):
        Reminder=temp % 10
        reverse =(reverse * 10)+Reminder
        temp=temp//10
        if(num==reverse):
            print("%d" %num,end=' ')

######################################################################
# Q2.	 Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that 
  #  Add 10 to the even number and multiply with 5 if it is odd number in the list1.
      
# list of numbers 
list1 = [3, 4, 5, 6, 7, 8] 
  
# iterating each number in list 
for num in list1: 
      
    # checking condition 
    
    if num % 2 == 0:                    # Checking for even condition
        print(num+10, end = " ")
        
    if num % 2 != 0:                    # Checking for odd condition
       print(num*5, end = " ") 
       
###############################################################################
# Q3.	Consider a list [2,3,4,5,6]. Find the total sum of cumulative products of all the numbers in the list.
  #  (sum= 2*3 + 2*3*4 +....) 
    
def cumprod(lst):
    results = []
    cur = 1
    for n in lst:
        cur *= n
        results.append(cur)
    return results

lst = [2,3,4,5,6]
print (cumprod(lst))

###############################################################################
# Q4.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) 
  #  and other list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
 #   Create a dictionary such that list2 are keys and list 1 are values. 
    
def Convert(list):
    res_dct = {list2[i]: list1[i] for i in range(0,10)}
    return res_dct
         
# Driver code
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['zero','one','two','three','four','five','six','seven','eight','nine']
print("Dictionary: ", Convert(list))

###############################################################################