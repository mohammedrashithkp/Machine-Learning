#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ### Basic Graph

# In[48]:


#Defining the x and y axes
x=[0,1,2,3,4]
y=[0,2,4,6,8]

# Resize the graph in terms of ratio and pixels
plt.figure(figsize=(5,3),dpi=100)

#Customising graphs with different parameters both in long form and shorthand form
##plt.plot(x,y,label='2x',color='green',marker='.',markersize=10,markeredgecolor='blue',linestyle='--')
plt.plot(x,y,'g.--',label='2x')



#Line Number 2 
x2 = np.arange(0,4.5,0.5)
y2=x2**2

#The first statement takes point excluding 5 which is why the next one starts at 4 so that it takes 5
plt.plot(x2[:5],y2[:5],'red',label='x^2')
plt.plot(x2[4:8],y2[4:8],'b--',label='x^2')

#Making a title and labels for the graph
plt.title('Our First Graph',fontdict={'fontname':'Comic Sans MS'})
plt.xlabel('X axis')
plt.ylabel('Y axis')

#Making the ticks or the scales that we usually uses on the labs
plt.xticks([0,1,2,3,4])
#plt.yticks([0,2,4,6,8,10])

plt.legend()

#Saving the figure as a png with a defined clarity in the same workspace as the notebook
plt.savefig('mygraph.png',dpi=300)

#Show plot
plt.show()


# ### Bar Chart

# In[81]:


labels=['A','B','C']
values = [1,4,3]

plt.figure(figsize=(6,4),dpi =100)

bars = plt.bar(labels,values,color='red')


# bars[0].set_hatch('/')
# bars[1].set_hatch('*')
# bars[2].set_hatch('-')
patterns=['/','*','-']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.title('Our First Barchart',fontdict={'fontname':'Comic Sans MS'})
plt.xlabel('X axis')
plt.ylabel('Y axis')



plt.savefig('barchart.png',format="png",dpi=300)


plt.show()


# ### Real World Examples

# In[34]:


gas=pd.read_csv('gas_prices.csv')

plt.figure(figsize=(8,5))

# x=gas.Year
# plt.plot(x,gas.USA,'r.-',label='USA')
# plt.plot(x,gas['UK'],'g.-',label='UK')


for country in gas:
    if country != 'Year' :
        plt.plot(gas.Year,gas[country],marker='.',label=country)

plt.xticks(gas.Year[::3])
plt.xlabel("Years")
plt.ylabel("Gas Price in USD")
plt.title("Gas prices over time(In USD)")

plt.legend()

plt.show()


# ### FiFa Data

# In[35]:


df=pd.read_csv('fifa_data.csv')
df.head()


# #### Histogram

# In[52]:


bins=[40,50,60,70,80,90,100]
plt.figure(figsize=(8,4),dpi=300)

plt.hist(df.Overall,bins=bins,color='green')



plt.xticks(bins)
plt.xlabel("Skill level")
plt.ylabel("Number of Players")
plt.title("Distribution of Player Skills in FIFA")

plt.show()


#  ### Pie Chart

# #### Preferred Foot

# In[79]:


left = df.loc[df['Preferred Foot']=='Left'].count()[0]
right = df.loc[df['Preferred Foot']=='Right'].count()[0]
# print(f' left {left} and right {right}')

plt.pie([left,right],labels=['Left','Right'],colors=['#abcdef','#aabbcc'],autopct='%.2f %%')

plt.title("Preferred Foot among FiFa Players")
plt.legend()
plt.show()


# #### Weight Distribution Pie Chart

# In[96]:


df.Weight=[int(x.strip('lbs'))  if type(x)==str else x for x in df.Weight]

plt.style.use('ggplot')

light = df.loc[df['Weight']< 125].count()[0]
light_med = df.loc[(df['Weight']>= 125) & (df['Weight'] < 150) ].count()[0]
medium = df.loc[(df['Weight']>= 150) & (df['Weight'] < 175)].count()[0]
medium_heavy = df.loc[(df['Weight']>= 175) & (df['Weight'] < 200 )].count()[0]
heavy = df.loc[df['Weight']> 200].count()[0]

plt.pie([light,light_med,medium,medium_heavy,heavy],
        labels=['light','light_med','medium','medium_heavy','heavy'],
        autopct='%.2f %%',
        pctdistance=0.8,
        explode=[.4,.1,0,0,.4]
       )

plt.title("Weight Distribution  of FIFA Players (in lbs)")
plt.show()


# ### Box PLot

# In[114]:


plt.style.use('default')
plt.figure(figsize=(5,8))

barcelona = df.loc[df['Club']=='FC Barcelona']['Overall']
madrid = df.loc[df['Club']=='Real Madrid']['Overall']
revs=df.loc[df['Club']=='New England Revolution']['Overall']

labels=['FC Barcelona','Real Madrid','NE Revolution']
boxes = plt.boxplot([barcelona,madrid,revs],labels=labels,patch_artist=True,medianprops={'linewidth':2})


for box in boxes['boxes']:
    box.set(color='#4286f4',linewidth=2)
    box.set(facecolor='#e0e0e0')
    



plt.title('Professional Football Team Comparison')
plt.ylabel('Overall FiFa Rating')
plt.show()


# In[ ]:




