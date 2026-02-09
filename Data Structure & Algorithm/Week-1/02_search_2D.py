import numpy as np

twoDarray = np.array([[11, 15, 10, 6],
                      [10, 14,11, 5],
                      [12,17,12,8],
                      [15, 18,14,9]])

def search2DArray(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                print(f"Target value {target} locates at RowIndex: {i} and ColIndex: {j}.")
    return "Element Not Found!"

print(search2DArray(twoDarray, 9))

print(search2DArray(twoDarray, 37))