import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


num_timesteps = 300 # length of time series
np.random.seed(0) # same data for every runtime

# random data (like white noise)
y = np.random.normal(loc=0, scale=1, size=num_timesteps)

# Create timesteps for index in time series dataframe
ts = pd.date_range(start="2026-01-01", periods=num_timesteps, freq="D")

# create df with time index
df = pd.DataFrame(data={"y":y}, index=ts)


# White noise Plotting
df.plot(figsize=(10, 5))
plt.title("White Noise")
plt.ylabel("y")
plt.xlabel("Time Stamps")
plt.grid()
plt.tight_layout()

# create a copy

df_ = df.copy()

plot_pacf(
    x = df_["y"],
    method='ywmle',
    lags = 30,
    alpha=0.05,
    auto_ylims=True)
plt.title("Partial Autocorrelation of White Noise")
plt.ylabel("Partial autocorrelation")
plt.xlabel("Lag")
plt.tight_layout()

#%%
# Import dataset

df = pd.read_csv('retail_sales.csv',
                 parse_dates=['ds'],
                 index_col=['ds'])

df.plot(y='y', marker='.', figsize = [10,5])
plt.title("Retail Sales")
plt.ylabel("Sales")
plt.xlabel("Time")



plot_pacf(
    x = df["y"],
    method='ywmle',
    lags = 30,
    alpha=0.05,
    auto_ylims=True)
plt.title("Partial Autocorrelation of White Noise")
plt.ylabel("Partial autocorrelation")
plt.xlabel("Lag")
plt.tight_layout()

#%%



























