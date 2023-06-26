N = int(input())
pre_line = []

for i in range(1, N+1):
    if i == 1:
        print(1)
        continue
    if i == 2:
        print(1, 1)
        pre_line.append(1)
        pre_line.append(1)
        continue
    temp = []
    for j in range(1, i+1):
        if j == 1 or j == i:
            temp.append(1)
            continue
        temp.append(pre_line[j-1-1] + pre_line[j-1])
    for j in temp:
        print(j, end=" ")
    if i != N:
        print("")
    pre_line = temp.copy()
