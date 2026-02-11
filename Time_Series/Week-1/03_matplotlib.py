import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)

y = x ** 2

#%%
# How we plot line plot
plt.plot(x, y)
plt.xlabel('X label')
plt.ylabel('y label')
plt.title('Title')
plt.show()

#%% 

# Scatterplot

plt.scatter(x,y)
plt.xlabel('X label')
plt.ylabel('y label')
plt.title("Scatter Plot")

#%%

# Sub-plot

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title 1')

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title 2')

plt.suptitle("Big Title") # Super title

plt.savefig('my_figure.png', dpi=300)


#%%

# Figure

plt.figure() # empty canvas
plt.plot(x, x**2, label='X squared')
plt.plot(x, x**3, label='X cubed')
plt.title('Title')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.legend(loc='best')
plt.show()

#%%
















