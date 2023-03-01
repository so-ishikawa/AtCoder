N, M = map(int, input().split())
d_list = list(map(int, input().split()))

can_reach_list = [False] * N * 2
can_reach_list[0] = True

for i in range(1, N+1):
    can_reach_flag = False
    for j in range(M):
        if i - d_list[j] < 0:
            continue
        if not can_reach_list[i - d_list[j]]:
            continue
        can_reach_flag = True
    can_reach_list[i] = can_reach_flag
if can_reach_list[N]:
    print("Yes")
else:
    print("No")
# print(can_reach_list)
