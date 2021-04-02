# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:11:41 2021

@author: Ayush
"""

  # Problem 1: Construct 2 lists containing all the available data types  
  #(integer, float, string, complex and Boolean) and do the following.

list1 = ["India", 2+3j, 33, 56.2,False]
list2 = ["Bangalore", 54.2,22,4+2j, True, False, False]

#a.	Create another list by concatenating above 2 lists
list3 = list1 + list2
print(list3)

# b.	Find the frequency of each element in the concatenated list.
for i in list3:
    print(list3.count(i))
len(list3)

#c.	Print the list in reverse order.
list3.reverse()
print(list3)


###########################################################

#Problem 2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set
# and 5 to 15 in other set)

S1 = {1,2,3,4,5,6,7,8,9,10}
S2 = {5,6,7,8,9,10,11,12,13,14,15}

#a.	Find the common elements in above 2 Sets.

Intersect = S1.intersection(S2)
print("Common Element/Intersection: ", Intersect)

#b.	Find the elements that are not common.

Non_common = S1.symmetric_difference(S2)

print("NON Common Element i.e Union of S1 U S2: ", Non_common)

#c.	Remove element 7 from both the Sets.
S1.remove(7)
print(S1)
S2.remove(11)
print(S2)


###################################################################3

#3.	Create a data dictionary of 5 states having state name as key and 
#number of covid-19 cases as values.

Covid_19 = {'Bangalore': 56545, 'Uttar Pradesh': 12340, 'Delhi': 100000,
           'Tamil Nadu': 50090, 'Kerala':56564}

#a.	Print only state names from the dictionary.

Covid_19.keys()

#b.	Update another country and it’s covid-19 cases in the dictionary.

Covid_19['UK'] = 565643
Covid_19['US'] = 879876
Covid_19['Italy'] = 200021
print(Covid_19)
Covid_19
