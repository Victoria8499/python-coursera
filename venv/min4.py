def min4(a, b, c, d):
    a = min(a, b)
    a = min(a, c)
    a = min(a, d)
    return a
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min4(a, b, c, d))
