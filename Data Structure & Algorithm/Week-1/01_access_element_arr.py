from array import *
arr1 = array('i', [1,2,3,4,5,6])

def access_element(array, index):
    if index > len(array):
        print("Value Error: No element by given index")
    else:
        print(array[index]) 
    
access_element(arr1, 2)

access_element(arr1, 9)