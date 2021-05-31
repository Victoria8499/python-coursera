a = int(input())
myList = []
if a == 1:
    print("1")
elif a == 2:
    print("1 2")
else:
    for i in range(a):
        for j in range(i):
            myList.append(i)
print(*myList[0:a])

'''
n = int(input())
itog = []
for i in range(1, n + 1):
    for j in range(i):
        itog.append(i)
print(*itog[:n])
'''