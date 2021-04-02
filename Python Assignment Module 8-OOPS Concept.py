# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:57:02 2021

@author: Ayush
"""

# Q1.	Construct a class which takes in 3 arguments first name, last name and age.
  #  And create an instance of that class.

import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
     
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Ayush",
    "Chitrey",
    datetime.date(1992, 12, 10), # year, month, day
    
)

print("First Name : ",person.name)
print("Last Name : ",person.surname)
print("Age : ",person.age())

###############################################################################
  # Q2.	Construct an example for Inheritance.

#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

class Parent:
     def __init__(self , fname, fage):
          self.firstname = fname
          self.age = fage
     def view(self):
         print(self.firstname , self.age)
class Child(Parent):
     def __init__(self , fname , fage):
          Parent.__init__(self, fname, fage)
          self.lastname = "Chitrey"
     def view(self):
          print("First Name : " , self.firstname)
          print("Last Name : " , self.lastname) 
          print("Age : ", self.age)
ob = Child("Ayush" , '29')
ob.view()

###############################################################################
  # Q3.	Explain Polymorphism in Python? Construct an example for Polymorphism.   

# Polymorphism means the ability to take various forms.
# It is the ability of an object to adapt the code to the type of the data it is processing.
# It is a built-in feature.
# Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
# Polymorphism means same function name (but different signatures) being uses for different types.,
# (i.e.)it helps to describe an action regardless of the type of objects.
    
class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
  
    def language(self): 
        print("Hindi is the most widely spoken language of India.") 
  
    def type(self): 
        print("India is a developing country.") 
  
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
  
    def language(self): 
        print("English is the primary language of USA.") 
  
    def type(self): 
        print("USA is a developed country.") 
  
obj_ind = India() 
obj_usa = USA() 

for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type() 
    
###############################################################################

