#!/usr/bin/env python
# coding: utf-8

# Name - Kanak Kawade

# In[3]:


import pandas as pd
# import libraries


# In[ ]:


# Step 1: Load the data set
data = pd.read_csv('student.csv')


# In[73]:


# Step 2: Explore the data
print(df.head())  # Display the first few rows


# In[74]:


print(df.info())  # Summary of the data set


# In[76]:


# Step 3: Handle missing values
print(df.isnull().sum())  # Check for missing values in each column


# In[77]:


df = df.dropna()  # Remove rows with missing values


# In[80]:


num_duplicates = df.duplicated().sum()
print(num_duplicates)


# In[81]:


# Step 4: Remove duplicates
df = df.drop_duplicates()


# In[89]:


# Check the data types of each column
print(df.dtypes)


# In[83]:


# Step 5: Correct inconsistencies
df['Gender'] = df['Gender'].replace({'male': 'M', 'female': 'F'})


# In[85]:


# Step 6: Validate data ranges (assuming 'MathScore' is a numerical column)
df = df[df['MathScore'] >= 0]  # Remove negative values or other outliers


# In[86]:


# Step 7: Encode categorical variables (if needed)
df['Gender'] = df['Gender'].astype('category')
df['ParentEduc'] = df['ParentEduc'].astype('category')


# In[87]:


# Step 8: Feature engineering (example: calculating 'GradeAverage')
df['GradeAverage'] = df[['MathScore', 'ReadingScore', 'WritingScore']].mean(axis=1)


# In[91]:


minimum_value = df['GradeAverage'].min()
print(minimum_value)


# In[93]:


# Step 9: Rechecking null values
print(df.isnull().sum()) 


# In[88]:


# Step 10: Validate cleaned data
print(df.head())  # Display the cleaned data set


# In[92]:


# Save the cleaned data to a new file (optional)
df.to_csv('cleaned_student_data.csv', index=False)


# In[ ]:




