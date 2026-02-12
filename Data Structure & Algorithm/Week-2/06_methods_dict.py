# Method Dictionary


myDict = {'Name':'Mg Mg', 'Age':21, 'Address':'Sagaing', 'education':'data science'}

# Just to remind
# copy before doing anything to dictionary
myDict2 = myDict.copy()
# print(myDict)
# print(myDict2)


print(myDict2.items())


print(myDict2.keys())

#------------------------------------------------

# print(myDict2.popitem())

# Set default
# if name1 exists, it will not added
print(myDict2.setdefault('name1', 'added'))
print(myDict2)

#------------------------------------------------

# Add the new dict to existing dict
newDict = {'a':1, 'b':2, 'c':3,}
myDict.update(newDict)
print(myDict)

#------------------------------------------------


