a = list(map(int, input().split()))
max = a.index(max(a))
min = a.index(min(a))
a[max], a[min] = a[min], a[max]
print(*a)
