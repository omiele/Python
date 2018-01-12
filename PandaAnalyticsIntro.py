
# coding: utf-8

# In[ ]:

# Using Panda Package for Analytics in python

#The code uses census data from the [United States Census Bureau](https://www.census.gov/data/datasets/2016/demo/popest/counties-total.html). Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2016. A copy of the data description document [co-est2016-alldata.pdf](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2016/co-est2016-alldata.pdf) has been provided in the A1 folder.

#The census dataset (census.csv) has been loaded below as `census_df`. This data is available in https://www.dropbox.com/s/t65iv729b7ph2nt/co-est2016-alldata.csv?dl=0


# In[1]:

import pandas as pd


# In[3]:

col_names = ['SUMLEV','DIVISION','STNAME','CTYNAME',  
             'POPESTIMATE2010', 'POPESTIMATE2011',
             'POPESTIMATE2012', 'POPESTIMATE2013',
             'POPESTIMATE2014', 'POPESTIMATE2015',
             'POPESTIMATE2016', 'NPOPCHG_2016']
census_df = pd.read_csv('data/co-est2016-alldata.csv', 
                        encoding='latin1', 
                        usecols=col_names)
census_df.head()


# ### B0: (example)
# What are the state population values for the first state in `census_df` ?
# 
# *This function should return a Series.*
# 
# >NOTE: You should write your whole answer within the function provided. For grading purposes the value returned by each question's function will be compared against that questions expected value.
# 

# In[3]:

def b0():
    state_df = census_df[census_df['SUMLEV'] == 40]
    return state_df.iloc[0]

b0()


# ### B1:
# Which five states have the most counties? (hint: consider the SUMLEVEL key carefully! You'll need this for future questions too...)
# 
# *This function should return a series.*

# In[77]:

def b1():
    county_df = census_df.groupby("STNAME").size().sort_values(ascending=False)
    new_d = pd.DataFrame(county_df)    
    return new_d.head()
   


# In[78]:

b1()


# ### B2:
# Which county had the largest numeric change in resident population from 7/1/2015 to 7/1/2016? (hint: review the PDF data document, co_est2016-alldata. )
# 
# *This function should return a series object.*

# In[104]:

def b2():
    census_df['Sub'] = census_df['POPESTIMATE2015']-census_df['POPESTIMATE2016']
    census_df['Sub'] = census_df['Sub'].abs()
    maximum = census_df.loc[census_df['Sub'].idxmax()]
    
    
    return maximum['CTYNAME']


# In[105]:

b2()


# ### B3:
# Only including the five least populous counties for each state, what are the five least populous states? Use `POPESTIMATE2016`.
# 
# *This function should return a list of five state names in order of lowest population to highest.*

# In[110]:

def b3():
    df = census_df.sort_values(['POPESTIMATE2016'], ascending=True)

    return df['STNAME'].head()


# In[111]:

b3()


# ### B4:
# In this datafile, the United States is broken up into nine divisions using the "DIVISION" column. 
# 
# Create a query that finds the counties that belong to divisions 8 or 9, whose name starts with the letter 'Y', and whose POPESTIMATE2016 was greater than their POPESTIMATE 2015.
# 
# *This function should return a 8x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).*

# In[156]:

def b4():
    df = pd.DataFrame(census_df)
    new_data = df.loc[(df.DIVISION == 8) | (df.DIVISION == 9) & (df.CTYNAME.str[0] == "Y") & (df.POPESTIMATE2016 > df.POPESTIMATE2015), ['STNAME', 'CTYNAME']]
    return new_data


# In[157]:

b4()


# In[ ]:



