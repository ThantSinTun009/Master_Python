nums = [0, 1, 1, 0]

output=[]
empty_list = []

for i in nums:
    if i in empty_list:
        output.append(i)
    empty_list.append(i)

print(output)