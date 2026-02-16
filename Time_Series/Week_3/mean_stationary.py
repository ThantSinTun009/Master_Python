import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Step 1
# Import data for mean_stationarity

df = pd.read_csv('Week_3/mean_stationary_data.csv')
df.head()

df['date'] = pd.to_datetime(df['date'])



# Calculate mean

mean = np.mean(df['customers'])


# Plot the mean stationarity on line plot

plt.figure(figsize=(12, 5))
plt.plot(df['date'], df['customers'])
plt.axhline(mean, color='r', linestyle='--', label='Overall Mean')
plt.title('Mean Stationarity')
plt.xlabel('Date')
plt.ylabel('Number of Customers')
plt.show()


















