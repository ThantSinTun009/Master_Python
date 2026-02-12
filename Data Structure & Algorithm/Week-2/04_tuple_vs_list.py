# Tuples vs Lists


List1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

List1[1] = 3

# print(List1)

init_tuple = ()
print(init_tuple.__len__())

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a == init_tuple_b)

init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print(init_tuple_a == init_tuple_b)

print(init_tuple_a + init_tuple_b)

#####################################################

# Tuple Comprehension

squares_tuple = tuple(x**2 for x in range(5))
print(squares_tuple)

cube_tuple = tuple(x**3 for x in [1, 2, 5])
print(cube_tuple)

#####################################################

# Tuple embagging

init_tuple = [(0, 1), (1, 2), (2, 3)]
# (0, 1) = _, n

result = sum(n for _,n in init_tuple)
print(result)


