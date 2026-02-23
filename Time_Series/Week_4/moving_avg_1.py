import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Week_3/retail_sales.csv',
                 parse_dates=['ds'],
                 index_col=['ds'])
df.head()

#%%

df.plot(y='y', marker='.', figsize=[10, 5])
plt.title("Retail Sales")
plt.xlabel("Sales")
plt.ylabel('Time')


#%%

# Moving average - Order of 3
window_size = 3 
ma_3 = df.rolling(
    window = window_size,
    center=True
    ).mean()

ma_3.rename(columns={'y':'3-MA'}, inplace=True)
# ma_3.head()

# Plot the result
fig, ax = plt.subplots(figsize=[12, 5])

df.plot(ax=ax, marker='.')
ma_3.plot(ax=ax, color='r', alpha=0.75)

ax.set_title("Retail Sales with Moving Average")
ax.set_xlabel("Time")
ax.set_ylabel("Retail Sales")


#%%

# Moving average - Order of 4
df1 = df.copy()

df1['4-MA'] = df1.rolling(window=4).mean()

# 4-MA do not have center so 

df1['2x4_MA'] = df1['4-MA'].rolling(window=2).mean()

df1['result'] = df1['2x4_MA'].shift(-2)

df1.head()

#%%

window_size_12 = 12 
ma_2_12 = (df.rolling(window=window_size_12)
           .mean()
           .rolling(window=2)
           .mean()
           .shift(-window_size_12//2)
           )

# Rename
ma_2_12.rename(columns={'y', 'ma_2_12'}, inplace=True)

# Plotting
fig, ax = plt.subplots(figsize=[12, 5])

df.plot(ax=ax, marker='.')
ma_2_12.plot(ax=ax, color='r', alpha=0.75)


























