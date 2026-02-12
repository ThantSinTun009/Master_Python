# Delete an element from dictinary

myDict = {'Name':'Mg Mg', 'Age':21, 'Address':'Sagaing', 'education':'data science'}

# del myDict['Age']
# print(myDict)

# Remove last item
removed_ele = myDict.popitem()
print(myDict)
print(removed_ele)


# Clear all items
myDict.clear()
print(myDict)

