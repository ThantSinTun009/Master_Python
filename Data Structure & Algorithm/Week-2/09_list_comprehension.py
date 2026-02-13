myList = [1,2,3]
print(myList)

new_list = []

for i in myList:
    mul_2 = i * 2
    new_list.append(mul_2)
    
print(new_list)

# List Comprehension
newlist2 = [x * 3 for x in myList]
print(newlist2)

# String list comprehension
word = 'Apple'
word_list_compre = [letter for letter in word]
print(word_list_compre)









