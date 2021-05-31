n = list(map(int, input().split()))
j = 0
for i in n:
    if j % 2 == 0:
        print(n[j], end=" ")
    j += 1
