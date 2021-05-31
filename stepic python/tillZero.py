a = int(input())
b = a ** 2
c = a
if c == 0:
    print(c)

else:
    while c != 0:
        a = int(input())
        c += a
        b += a ** 2
print(b)