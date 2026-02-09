#%% Numpy
import numpy as np

first_array = np.array([[1,2,3], [4,5,6]])
first_array

A = np.array([[1,2], [3,4]])
B = np.array([[3,4], [5,7]])

#%% Multiplication

# Multiply a matrix by another matrix
# Element wise multiplication
C = A * B

# Matrix Multiplication
M = np.matmul(A, B)

# Check if results are the same
C == M

# same as matmul
D = np.dot(A, B)
D == M
D

E = np.multiply(A, B)
E

E == C

#%% Adding and substraction

sum1 = A + B
sum2 = np.sum(A)

subtract1 = A - B
sub2 = np.subtract(C, D)

borad_num = A + 3

borad_mat = np.array([[3,3], [3,3]])
borad_num

#%% Division


D2 = np.divide([12, 14, 15], 2)
D2

D_floor = np.floor_divide([12, 14, 15], 2)
D_floor

sq = np.math.sqrt(10)
sq

#%% Distribution

# standard normal
normal_d = np.random.standard_normal((3,4))
normal_d

uniform_d = np.random.uniform(1, 12, (3,4)) # lower bound & upper bound

# Generate float number
np.random.rand()

# generate random integer
Random_int = np.random.randint(1, 50, (2, 5))
Random_int

zero_matrix = np.zeros((3, 4))


one_matrix = np.ones((3, 4))

# Filter

filter_arr = np.logical_and(Random_int>30, Random_int<50) # mask
filter_arr

Filtered_int = Random_int[filter_arr]


#%% Summary statistics

Data_N = np.array([1,3,5,7,9])

Mean_N = np.mean(Data_N)
Mean_N

Median_N = np.median(Data_N)
Median_N

Var_N = np.var(Data_N)

Std_N = np.std(Data_N)




#%%



