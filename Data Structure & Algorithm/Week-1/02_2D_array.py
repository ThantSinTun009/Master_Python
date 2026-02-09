import numpy as np

# create 2D array
twoDarray = np.array([[11, 15, 10, 6],
                      [10, 14,11, 5],
                      [12,17,12,8],
                      [15, 18,14,9]])

print(twoDarray)

print('\n')

print("New 2D array")
new_2d_arr = np.insert(twoDarray, 0, [[1,2,3,4]], axis=0) # org_arr, index, new_arr, axis=0 (row-wise)
print(new_2d_arr)

# append function
newTwoDarray = np.append(twoDarray, [[2,2,2,2]], axis=0) # append to last row

print(newTwoDarray)