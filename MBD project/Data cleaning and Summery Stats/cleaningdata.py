# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 07:38:54 2020

@author: pelum
"""
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from pandas.api.types import is_string_dtype, is_numeric_dtype
import numpy as np
data = pd.read_csv("C:\\Users\\pelum\OneDrive - Emory University\\Fall 20'\\Big Data\\Final Project\\airtraffic.csv")


#storing all the unique states in a variable to use later for filtering  
data["State"].value_counts()
states = data["State"].unique()
states = list(states) 
print(states)

#reading in all the x variables were using for our models and filtering to only include states stored in the states variable to ensure data is consistent
tourist = pd.read_excel("C:\\Users\\pelum\\OneDrive - Emory University\\Fall 20'\\Big Data\\Final Project\\tourists.xlsx")
tourist.head()

t = tourist[tourist['State/Territory Visitation'].isin(states)]
t["State/Territory Visitation"].unique()

t.to_csv (r'C:\Users\pelum\OneDrive - Emory University\Desktop\new_tourists.csv', index = False, header=True)

pop =  pd.read_excel("C:\\Users\\pelum\\OneDrive - Emory University\\Fall 20'\\Big Data\\Final Project\\pop_density.xlsx")
pop =  pop[pop['State'].isin(states)]
pop['State'].unique()
pop.to_csv (r'C:\Users\pelum\OneDrive - Emory University\Desktop\new_pop.csv', index = False, header=True)

age = pd.read_csv("C:\\Users\\pelum\\OneDrive - Emory University\\Fall 20'\\Big Data\\Final Project\\age.csv")
age = age[age['State'].isin(states)]
age['State'].unique()
age.to_csv (r'C:\Users\pelum\OneDrive - Emory University\Desktop\new_age.csv', index = False, header=True)

gdp = pd.read_csv("C:\\Users\\pelum\\OneDrive - Emory University\\Fall 20'\\Big Data\\Final Project\\gdp.csv")
gdp = gdp[gdp["State"].isin(states)]
gdp["State"].unique()
gdp.to_csv (r'C:\Users\pelum\OneDrive - Emory University\Desktop\new_gdp.csv', index = False, header=True)

#reading in the calculated indegree, outdegree and pagerank for each airport 
central = pd.read_csv("C:\\Users\\pelum\\OneDrive - Emory University\\Desktop\\central.csv")
central["node"] = central["node"].astype(str)

#removing the index column
central =central.iloc[:,1:]
central.head()

#creating a new data frame to include only the airports with the highest enplanements from wikipedia https://en.wikipedia.org/wiki/List_of_airports_in_the_United_States
#if two or three airports had high enplanements in a city took the average and used that 
#changed the airport code to the state name 

central.loc[central["node"]=='JFK',"node"] = 'New York'
central.loc[central["node"]== 'LGA',"node"] = 'New York'
ny = central.loc[central['node']=='New York'].mean()

central.loc[central["node"]==  'FLL',"node"] = 'Florida'
central.loc[central["node"]==  'MIA',"node"] = 'Florida'
central.loc[central["node"]==  'MCO',"node"] = 'Florida'
fl = central.loc[central['node']=='Florida'].mean()

central.loc[central["node"]==  'LAX',"node"] = 'California'
central.loc[central["node"]==  'SFO',"node"] = 'California'
cal = central.loc[central['node']=='California'].mean()

central.loc[central["node"]==  'HNL',"node"] = 'Hawaii'
haw = central.loc[central['node']=='Hawaii'].mean()

central.loc[central["node"]==  'LAS',"node"] = 'Nevada'
nev = central.loc[central['node']=='Nevada'].mean()

central.loc[central["node"]==  'BOS',"node"] = 'Massachusetts'
mass = central.loc[central['node']=='Massachusetts'].mean()

central.loc[central["node"]==  'DFW',"node"] = 'Texas'
central.loc[central["node"]==  'IAH',"node"] = 'Texas'
tx = central.loc[central['node']=='Texas'].mean()

central.loc[central["node"]==  'ORD',"node"] = 'Illinois'
central.loc[central["node"]==  'MDW',"node"] = 'Illinois'
ill = central.loc[central['node']=='Illinois'].mean()

central.loc[central["node"]==  'EWR',"node"] = 'New Jersey'
nj = central.loc[central['node']=='New Jersey'].mean()

central.loc[central["node"]==  'SEA',"node"] = 'Washington'
wash = central.loc[central['node']=='Washington'].mean()

central.loc[central["node"]==  'ATL',"node"] = 'Georgia'
g = central.loc[central['node']=='Georgia'].mean()

central.loc[central["node"]==  'DCA',"node"] = 'Virginia'
central.loc[central["node"]==  'IAD',"node"] = 'Virginia'
v = central.loc[central['node']=='Virginia'].mean()

central.loc[central["node"]==  'DEN',"node"] = 'Colorado'
col = central.loc[central['node']=='Colorado'].mean()

central.loc[central["node"]==  'CLT',"node"] = 'North Carolina'
central.loc[central["node"]==  'RDU',"node"] = 'North Carolina'
nc = central.loc[central['node']=='North Carolina'].mean()

central.loc[central["node"]==  'DTW',"node"] = 'Michigan'
mich = central.loc[central['node']=='Michigan'].mean()

#combining all the values and creating a column called state to show which state is represented in each row
others = [ny,fl,cal,haw,nev,mass,tx,ill,nj,wash,g,v, col,nc,mich]
others = pd.DataFrame(others)
others.index()
others["state"]=["New York", "Florida","California", "Hawaii", "Nevada","Massachusetts","Texas","Illinois","New Jersey", 
             "Washington", "Georgia","Virginia", "Colorado", "North Carolina", "Michigan"]

#exporting new table to csv
others.to_csv (r'C:\Users\pelum\OneDrive - Emory University\Desktop\central_us.csv', index = False, header=True)


