N, W = map(int, input().split())
A_list = list(map(int, input().split()))

flag_list = [False]*W
flag_list.insert(0, "dummy")

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = A_list[i] + A_list[j] + A_list[k]
            if temp > W:
                continue
            flag_list[temp] = True

for i in range(0, N):
    for j in range(i+1, N):
        # for k in range(j+1, N):
        temp = A_list[i] + A_list[j]# + A_list[k]
        if temp > W:
            continue
        flag_list[temp] = True

for i in range(0, N):
    # for j in range(i+1, N):
    # for k in range(j+1, N):
    temp = A_list[i]# + A_list[j] + A_list[k]
    if temp > W:
        continue
    flag_list[temp] = True


print(flag_list.count(True))
