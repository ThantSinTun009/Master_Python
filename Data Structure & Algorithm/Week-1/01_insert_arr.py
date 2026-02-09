import array 

my_arr = array.array('i', [1,2,3,4,5])
print(my_arr)

my_arr.insert(5, 7) # index, inserted value
print(f'New array after inserting: {my_arr}')

my_arr.insert(6, 9)
print(my_arr)