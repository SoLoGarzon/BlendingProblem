#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pulp import *
df = pd.read_excel('C:/Users/owner/Desktop/O-R-1/fooddatayas.xlsx', sheet_name='Sheet1')
print(df)

#'prob' variable contains the problem data
prob = LpProblem("Celiac Diet Problem",LpMinimize)

#list of foods
food_items = list(df['Foods'])

print("Possible foods are\n"+"-"*100) #prints 100 -
for f in food_items:
    print(f,end=', ')

costs = dict(zip(food_items,df['Price/Serving']))  
size = dict(zip(food_items,df['Serving Size']))
calories = dict(zip(food_items,df['Calories']))
cholesterol = dict(zip(food_items,df['Cholesterol(mg)']))
fat = dict(zip(food_items,df['Total Fat(g)']))
fiber = dict(zip(food_items,df['Dietary Fiber(g)']))
protein = dict(zip(food_items,df['Protein(g)']))
vitA = dict(zip(food_items,df['Vit_A(IU)']))
zinc = dict(zip(food_items,df['Zinc(mg)']))
calcium = dict(zip(food_items,df['Calcium(mg)']))
iron = dict(zip(food_items,df['Iron(mg)']))


# In[15]:






# In[ ]:




