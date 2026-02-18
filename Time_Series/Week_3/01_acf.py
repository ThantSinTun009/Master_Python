import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf


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


#%%

# create a copy

df_ = df.copy()

# Compute the lag of the target
lag = 1
df_[f"y_Lag_{lag}"] = df_["y"].shift(periods=lag)


# Compute mean of the y of the df_
y_mean = df_["y"].mean()


# Numerator of acf equation
numerator = ((df_["y"] - y_mean) * (df_[f"y_Lag_{lag}"] - y_mean)).sum() 


# Denorminator of acf equation

denominator = ((df_["y"] - y_mean)**2).sum()


r = numerator / denominator
print(f"ACF: {r}")


r = {}
for lag in range(0, 13):
    df_ = df.copy()
    df_["y_lag"]  = df_["y"].shift(lag)
    y_mean = df_["y"].mean()
    numerator = ((df_["y"] - y_mean) * (df_["y_lag"] - y_mean)).sum() 
    denominator = ((df_["y"] - y_mean)**2).sum()
    r[lag] = numerator / denominator
    # print(f"ACF at lag {lag}: {r}")

acf_ = pd.Series(r)

# Stem plot
plt.figure(figsize=(12, 5))
plt.stem(acf_)
plt.title("Autocorrelation of white noise")
plt.ylabel("Autocorrelation")
plt.xlabel("Lag")
plt.tight_layout()


plot_acf(
    x = df["y"],
    lags = 30,
    alpha=0.05,
    auto_ylims=True);

plt.title("Autocorrelation of White Noise")
plt.ylabel("Autocorrelation")
plt.xlabel("Lag")

#%%


# ACF Plot with retail_sales


df = pd.read_csv('retail_sales.csv',
                 parse_dates=['ds'],
                 index_col=['ds'])

df.plot(y='y', marker='.', figsize = [10,5])
plt.title("Retail Sales")
plt.ylabel("Sales")
plt.xlabel("Time")


plot_acf(
    x = df["y"],
    lags = 30,
    alpha=0.05,
    auto_ylims=True);
plt.title("Autocorrelation of Retail Sales")
plt.ylabel("Autocorrelation")
plt.xlabel("Lag")









