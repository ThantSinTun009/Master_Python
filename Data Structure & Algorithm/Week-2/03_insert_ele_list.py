mylist = [1,2,3,4,5,6,7]
print(mylist)

# item assignment
mylist[2] = 33
print(mylist)


mylist[4] = 55
print(mylist)

# Inserting
mylist.insert(4, 15) # index, value
print(mylist) # not replace value, just change index


# Append list
newlist = [1, 3, 5, 7]
mylist.append(newlist)
print(mylist) # nested list



# Extend
newlist1 = [11, 12, 13, 14]
mylist.extend(newlist1)
print(mylist) # not nested list, just a list














