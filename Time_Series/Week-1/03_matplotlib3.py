import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('montly_electricity_consumption.csv')


data.head()


month = data.iloc[:, 0]
customer_A = data.iloc[:, 1]
customer_B = data.iloc[:, 2]

plt.figure()
plt.plot(month, customer_A)
plt.plot(month, customer_B)
plt.xticks(month, rotation=45)
plt.xlabel('Month')
plt.tight_layout()
plt.show()

##############################################

plt.figure()
plt.plot(month, customer_A, color='r', label='Customer A', marker='o')
plt.plot(month, customer_B, color='b', label='Customer B', marker='*')
plt.xticks(month, rotation=45)
plt.tight_layout()
plt.xlabel('Month')
plt.ylabel('KWh')
plt.title("Electricity Consumption Chart")
plt.legend()
plt.show()


#%%

# Subplot

plt.subplot(2, 1, 1)
plt.plot(month, customer_A, color='r', label='Customer A', marker='o')
plt.xlabel('Month')
plt.ylabel('KWh')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(month, customer_B, color='b', label='Customer B', marker='*')
plt.xlabel('Month')
plt.ylabel('KWh')
plt.legend()

plt.suptitle('Electricty Consumption Chart')

plt.tight_layout()

plt.show()

#%%

# Scatterplot

plt.scatter(month, customer_A, color='r', label='Customer A')
plt.scatter(month, customer_B, color='b', label='Customer B')
plt.xlabel('Month')
plt.ylabel('KWh')
plt.title("Scatter Plot of Electricity Consumption")
# plt.legned(loc=(0.1, 0.1))
plt.legend(loc='best')
plt.grid()
plt.xticks(month, rotation=45)
plt.tight_layout()
plt.show()

#%%

# Histogram

plt.hist(customer_A, bins=20, color='b', rwidth=0.8)
plt.xlabel('KWh')
plt.ylabel('Count')
plt.title('Histogram')
plt.show()

#%%

# Bar chart

plt.bar(month, customer_A, color='lightblue')
plt.xlabel('Month')
plt.ylabel('KWh')
plt.xticks(month, rotation=45)
plt.tight_layout()
plt.title('Electricity Consumption Bar Graph')
plt.show()

# Two customers in a single bar graph

import numpy as np

bar_width = 0.4
month_b = np.arange(1, 13)

plt.bar(month_b, customer_A, bar_width, color='r', label='Customer A')
plt.bar(month_b+bar_width, customer_B, bar_width, color='b', label='Customer B')
plt.title('Bar chart')
plt.legend(loc='upper left')
plt.xticks(month_b + (bar_width)/2, (month), rotation=45)
plt.tight_layout()
plt.show()


#%%




























