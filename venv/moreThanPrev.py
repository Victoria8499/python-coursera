n = list(map(int, input().split()))
for i in range(len(n)):
    if i > 0:
        if n[i] > n[i - 1]:
            print(n[i], end=" ")
