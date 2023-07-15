N, M = map(int, input().split())
temp = []
for i in range(N):
    f_list = list(map(int, input().split()))
    p = f_list.pop(0)
    c = f_list.pop(0)
    temp.append([p,c,f_list])

temp.sort(key=lambda x: x[0])

for j in range(len(temp)-1):
    for i in range(j+1, len(temp)):
        if not (set(temp[j][2]) >= set(temp[i][2])):
            continue
        if temp[i][0] > temp[j][0] or (set(temp[j][2]) - set(temp[i][2]) != set()):
            print("Yes")
            exit()
print("No")
exit()

