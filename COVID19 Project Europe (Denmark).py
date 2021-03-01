#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("coviddata.csv",index_col=0)
print(data.shape)
print(data.continent.value_counts())

#We will investigate the Denmark cases .
data2=data.loc[data["continent"]=="Europe"]
data_3=data2.loc[data2["location"]=="Denmark"]
print(data_3)


# In[43]:


total_deaths=data_3["total_deaths"].sum()
print(total_deaths)
total_cases=data_3["total_cases"].sum()
print(total_cases)


# In[44]:


cardiovasc_death_rate=data_3["cardiovasc_death_rate"].sum()
diabetes_prevalence=data_3["diabetes_prevalence"].sum()
female_smokers=data_3["female_smokers"].sum()
male_smokers=data_3["male_smokers"].sum()
print(cardiovasc_death_rate,diabetes_prevalence,female_smokers,male_smokers)
female_smokers_per=female_smokers/total_cases
print(female_smokers_per*100)
male_smokers_per=male_smokers/total_cases
print(male_smokers_per*100)
smokers=female_smokers + male_smokers
non_smokers=total_cases-smokers
smokers_per=smokers/total_cases
non_smokers_per=non_smokers/total_cases
print(smokers_per*100,non_smokers_per*100)


# In[45]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
mylabels = ["Smokers", "Non_smokers"]
plt.title("Percentages of Smokers and Non smokers, infected with COVID9 ")
y = np.array([smokers_per*100+1,non_smokers_per*100-1])
ax.pie(y, labels = mylabels, autopct='%1.2f%%')
plt.legend(loc='upper right')
plt.show()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
mylabels = ["Male smokers", "Female smokers"]
plt.title("Percentages of Male and Female Smokers, infected with COVID9 ")
y = np.array([male_smokers/smokers,female_smokers/smokers])
ax.pie(y, labels = mylabels, autopct='%1.2f%%')
plt.legend(loc='upper right')
plt.show()


# In[ ]:




