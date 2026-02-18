# Subplots

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/Lenovo/Desktop/time_series_a/Week_3/stationary_vs_nonstationary_data.csv')

# Formatting datetime
df['date'] = pd.to_datetime(df['date'])


rolling_mean = df['non_stationary'].rolling(30).mean()


# Create plot
plt.figure(figsize=(14,5))

# Stationary
plt.subplot(1, 2, 1)
plt.plot(df['date'], df['stationary'], alpha=0.7)
plt.axhline(y=df['stationary'].mean(), color='r', linestyle='--')
plt.title("Weakly stationary (Constant Mean & Variance)")
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True, alpha=0.3)

# Non-stationary
plt.subplot(1,2,2)
plt.plot(df['date'], df['non_stationary'], alpha=0.7, color='orange')
plt.plot(df['date'], rolling_mean, color='r', linestyle='--', linewidth=2)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title("Non-stationary Plot")
plt.grid(True, alpha=0.3)
plt.tight_layout()







