a = list(map(str, input().split()))
c = []
cnt = 0
while a[0] != 'end':
    b = [int(a[i]) for i in range(len(a))]
    c.append(b)
    cnt += 1
    a = list(map(str, input().split()))

newList = []
for i in range(len(c)):
    length_str = len(c[i])
    i_of_top_element = len(c) - 1 if i == 0 else i - 1
    i_of_bottom_element = 0 if i == len(c) - 1 else i + 1
    newList.append([])
    for j in range(length_str):
        j_of_left_element = length_str - 1 if j == 0 else j - 1
        j_of_right_element = 0 if j == length_str - 1 else j + 1
        sum = c[i][j_of_left_element] + c[i_of_top_element][j] + c[i][j_of_right_element] + c[i_of_bottom_element][j]
        newList[i].append(str(sum))
    print(' '.join(newList[i]))
