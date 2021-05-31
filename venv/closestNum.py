size = int(input())
myList = list(map(int, input().split()))
num = int(input())
i = 0
b = []
while i < size:
    b.insert(i, myList[i] - num)
    i += 1
    closNumIndex = b.index(min(b, key=abs))
print(myList[closNumIndex])
