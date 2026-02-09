from array import *

arr1 = array('i', [1,2,3,4,5,6,7])

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return("Not Found")
        
print(f'Index Number: {linear_search(arr1, 7)}')
print(f'Index Number: {linear_search(arr1, 9)}')