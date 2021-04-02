# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:57:02 2021

@author: Ayush
"""

 #  Q1.	Write a function that eliminates all the punctuation symbols, html tags, etc. in the given text.
  #    It should return plain text containing alpha numeric characters.
   #   Text="NumPy,<1> pandas ?,matplotlib; |,seaborn# SciPy* etc.. are few &Python packages) that are) frequently (/used |@for text% preprocessing$.” 

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|1'''

text= ''' "NumPy,<1> pandas ?,matplotlib; |,seaborn# SciPy* etc.. are few &Python packages) that are) frequently (/used |@for text% preprocessing$.” '''

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in text:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

###############################################################################
 #  Q2. For the dataset “Indian_cities”, 
  #    a)	Find out top 10 states in female-male sex ratio
    #  b)	Find out top 10 cities in total number of graduates
   #   c)	Find out top 10 cities and their locations in respect of total effective_literacy_rate.

import pandas as pd

indiancities = pd.read_csv("C:\\Users\\AyushChitrey\\Data_Science\\Python_Programming\\Indian_Cities_Dataset.csv")
indiancities

# A.
print("Top 10 States in female-male sex ratio")
top10_states = indiancities.sort_values(by='state_name', ascending = False)
top10_states_sex_ratio = top10_states.head(10)
top10_states_sex_ratio

# B.
print("Top 10 cities in total number of graduates")
top10_cities = indiancities.sort_values(by='total_graduates', ascending = False)
top10_cities_total_graduates = top10_cities.head(10)
top10_cities_total_graduates

# C.
print("Top 10 cities and their locations in respect of total effective_literacy_rate")
top10_cities1 = indiancities.sort_values(by='effective_literacy_rate_total', ascending = False)
top10_cities_total_literacy = top10_cities1.head(10)
top10_cities_total_literacy

###############################################################################
# Q3.	For the data set “Indian_cities”
 #   a)	Construct histogram on literates_total and comment about the inferences
 #   b)	Construct scatter plot between male graduates and female graduates
 #   c)	Construct Boxplot on total effective literacy rate and draw inferences
 #   d)	Find out the number of null values in each column of the dataset and delete them.

import pandas as pd
import matplotlib.pyplot as plt

indiancities = pd.read_csv("C:\\Users\\AyushChitrey\\Data_Science\\Python_Programming\\Indian_Cities_Dataset.csv")
indiancities

# A.
plt.hist(indiancities.literates_total)   # histogram

# B.
x = indiancities.male_graduates
y = indiancities.female_graduates
plt.scatter(x,y)    # scatterplot

# C.
plt.boxplot(indiancities.effective_literacy_rate_total)   # boxplot

# D.
details = pd.DataFrame(indiancities, columns =['name_of_city','state_code','state_name','dist_code','population_total','population_male','population_female','0-6_population_total','0-6_population_male','0-6_population_female','literates_total','literates_male','literates_female','sex_ratio','child_sex_ratio','effective_literacy_rate_total','effective_literacy_rate_male','effective_literacy_rate_female','location','total_graduates','male_graduates','female_graduates'],
                                       index =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']) 
print(details)

# show the boolean dataframe             
print(" \nshow the boolean Dataframe : \n\n", details.isnull()) 
  
# Count total NaN at each column in a DataFrame 
print(" \nCount total NaN at each column in a DataFrame : \n\n", details.isnull().sum()) 

# Count total NaN in a DataFrame 
print(" \nCount total NaN in a DataFrame : \n\n", details.isnull().sum().sum()) 

# drop all rows with any NaN and NaT values
details1 = details.dropna()
print(details1)

###############################################################################




