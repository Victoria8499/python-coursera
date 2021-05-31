n = list(map(int, input().split()))
j = 0
max = n[0]
for i in range(len(n)):
    if n[i] >= max:
        max = n[i]
        j = i
print(max, j, end=" ")
