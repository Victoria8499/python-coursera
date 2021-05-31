n = list(map(int, input().split()))
min = 1000
for i in range(len(n)):
    if n[i] > 0:
        if n[i] < min:
            min = n[i]
print(min)
