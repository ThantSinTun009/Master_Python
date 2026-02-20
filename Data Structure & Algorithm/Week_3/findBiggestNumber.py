def findBiggestNumber(list):
    max = list[0] # ----------------> O(1)
    for i in range(len(list)): # ------------> O(N)
        if list[i] > max: # --------> if statement ----> O(1)
            max = list[i] # -------------> assignment ----> O(1)
    return max # ----------------> O(1)


list1 = [1,2, 5]
print(findBiggestNumber(list1))


# O(1) --> non dominant so our time complexity is O(N)