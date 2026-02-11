import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('global_temp_index.csv')
data.head()

# year = data['year']
# temp_index = data['temperature_index']

year = data.iloc[:, 0]
temp_index = data.iloc[:, 1]


plt.plot(year, temp_index)
plt.xlabel('Year')
plt.ylabel('Temp Index')
plt.xticks(year, # to be more specific for year
           rotation=45)
plt.title('Global Warming', family='Times New Roman')
plt.tight_layout() # for not overlap

plt.savefig('Global_Warming.png', dpi=300)

plt.show()

##########################################

























