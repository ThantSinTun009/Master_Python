import pandas as pd

#%% Series (1D)

"""Series"""

Age= pd.Series([10,20,30,40], index=['age1', 'age2', 'age3', 'age4'])

Age.age3

Age.age2

# Filtering values of the Series
Filter_age = Age[Age > 10]
Filter_age


Filter_age2 = Age[(Age > 10) & (Age < 40)]
Filter_age2

# between
filter_age3 = Age[Age.between(20, 30)]
filter_age3

# Calling values of the Series
Age.values

# Calling indexes of the Series
Age.index

#%% DataFrame (Multiple D)

"""DataFrame"""

# Create DataFrame

import numpy as np

df = np.array([[29, 10, 8], [25, 8, 10], [27, 5, 3], [30, 9, 7]])

df

dataset = pd.DataFrame(df)

# Change index
data_set = pd.DataFrame(df, index=['S1', 'S2', 'S3', 'S4'])

# Add column labels
data_set = pd.DataFrame(df, index=['S1', 'S2', 'S3', 'S4'], columns=['Age','Grade1', 'Grade2'])
data_set

# Adding new columns
data_set['Grade3'] = [9, 6, 4, 2]

data_set

#%% Indexing

# .loc is label-based indexing and include the end
# .iloc is position, integer-based indexing and exclude the end

data_set.loc['S1']

data_set.loc['S1':'S2'] # include the end means both S1 and S2 is returned as output

# .iloc()
data_set.iloc[1, 2]

# all rows and 1 columns
data_set.iloc[:, 0]

data_set.iloc[:, 3]

data_set.iloc[:, 1:3] # Exclude the last: not include 3

data_set.iloc[:, :3]

data_set.iloc[1:3, :]

data_set.iloc[:3, :]

data_set.iloc[3, :]

filtered_data_set = data_set.iloc[:, 1:3]

#%% Drop & Replace

data_set_drop = data_set.drop('Grade1', axis=1)

data_set_change = data_set.replace(10, 12)

data_set_change2 = data_set.replace({30:10, 9:30})


data_set.head()

data_set.tail(2)

#%% Sort Values

data_set.sort_values(by=['Grade1'], ascending=True)

data_set.sort_values(by=["Age"], ascending=False)


# sorting with index numbers
data_set.sort_index(axis=0, ascending=False)

data_set.sort_index(axis=0, ascending=True)

# Rearrange data based on its index labels rather than values

#%% Importing dataset

df = pd.read_csv('household_electricity_consumption.csv')

df.head()

df.shape

df.to_csv('output1.csv')

# with unnecessary index like Unnamed: 0
df1 = pd.read_csv('output1.csv')
df1

df.to_csv('output2.csv', index=False)
df2 = pd.read_csv('output2.csv')
df2.head()

# 2 col indexing
two_col_df = df2.iloc[:, 1:3]


all_cols_not_last = df2.iloc[:, :-1]

last_col = df.iloc[:, -1]

#######################################

first_six_hours = df.iloc[:7, :]

















