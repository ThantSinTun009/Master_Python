# Search tuples

new_Tuple = ('a', 'b', 'c', 'd', 'e')

def search_ele_tuple(tuple, target):
    for i in range(0, len(new_Tuple)):
        if new_Tuple[i] == target:
            return f"The element is found at {i} index"
    return "The element is not found!"

print(search_ele_tuple(new_Tuple, 'e'))

print(search_ele_tuple(new_Tuple, 'n'))