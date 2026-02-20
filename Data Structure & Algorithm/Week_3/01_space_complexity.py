# Space complexity

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)

print(sum(3))

# Space complexity - 6 (constant)
# O (1)