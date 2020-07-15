#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
 
Skills1= set(r"C:\Users\user\Downloads\ResumeSkills.json")
Skills2 = set(r"C:\Users\user\Job Skills.json")

 
jd_Skills_1_2 = nltk.jaccard_distance(Skills1, Skills2)

 
 
print(jd_Skills_1_2, 'Jaccard Distance between JDSkills and ResumeSkills')

 


# In[ ]:




