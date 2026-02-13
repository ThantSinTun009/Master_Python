shoppingList = ['Milk', 'Cheese', 'Butter']

# print(shoppingList[2])

# Check
# print('Milk' in shoppingList)

# print('Coffee' in shoppingList)

# Fetch elements
for i in shoppingList:
    print(i)

print('\n')

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + '*'
    print(shoppingList[i])


empty_list = []
for i in empty_list:
    print('List is empty')

