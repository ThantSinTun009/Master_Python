myList = [-1, 10,-20, 2, -90, 60, -40, 45, 20]

positive_List = [number for number in myList if number > 0]
print(positive_List)

negative_List = [number for number in myList if number < 0]
print(negative_List)

# Q1. positive sqr
positive_sqr = [number ** 2 for number in myList if number > 0]
print(positive_sqr)

# Q2. Number multiply by number
num_mul = [number * number for number in myList if number > 0]
print(num_mul)

# Q3 .Number multiply by neg number
num_mul_neg = [number * number for number in myList if number < 0]
print(num_mul_neg)


# only positive, but zero to negative
new_list2 = [number if number > 0 else 0 for number in myList]
print(new_list2)

# List comprehension with function
def get_number(number):
    if number > 0:
        return number # could modify
    else:
        return "Negative"
    
new_list3 = [get_number(number) for number in myList]
print(new_list3)


# Language/Text Comprehension

sentence = 'My name is Jerry'

# letter = [letter for letter in sentence]
# print(letter)

# Consonants
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [letter for letter in sentence if is_consonant(letter)]
print(consonants)


# Vowels
def is_vowel(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() in vowels

vowels = [letter for letter in sentence if is_vowel(letter)]
print(vowels)













