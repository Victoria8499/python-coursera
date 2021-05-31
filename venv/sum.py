def sum(x, y):
    if x == 0:
        return y
    return sum(x - 1, y + 1)
a, b = int(input()), int(input())
print(sum(a, b))
