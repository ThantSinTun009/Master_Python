myList = [10, 20, 30,40,50,60,70,80,90]

def linear_search(list, target):
    for i, value in enumerate(list):
        if value == target:
            return f"The element is found at {i} index"
    return f"Target {target} not found"

print(linear_search(myList, 100))


















