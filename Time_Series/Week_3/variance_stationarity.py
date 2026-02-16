import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Week_3/variance_stationary_data.csv')


# Change datetime format
df['date'] = pd.to_datetime(df['date'])

mean = np.mean(df['temperature'])
variance = np.var(df['temperature'])


# Plot the mean stationarity on line plot
plt.figure(figsize=(12, 5))
plt.plot(df['date'], df['temperature'], color='b')
plt.axhline(mean, color='r', linestyle='--', label='Overall Mean')
std_dev = np.sqrt(variance)
plt.fill_between(df['date'],
                 mean - std_dev,
                 mean + std_dev,
                 alpha=0.2, color='gray',
                 label='+- 1 Std Dev')
plt.title('Variance Stationarity')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.show()








