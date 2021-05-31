a = list(map(int, input().split()))
c = 0
for i in range(a[1]):
    b = int(input())
    c += b
print(a[0] // c)