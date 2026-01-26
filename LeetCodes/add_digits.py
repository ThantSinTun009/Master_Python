num = 123


while num >= 10:
    output = 0
    while num > 0:
        output += num % 10
        num = num // 10
    num = output

print(num)
