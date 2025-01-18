from collections import deque
Q = int(input())
d = deque()
rui_sum = deque()
delete_sum = 0

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        d.append(query[1])
        if len(rui_sum) == 0:
            rui_sum.append(query[1])
        else:
            rui_sum.append(rui_sum[-1]+query[1])
        continue
    if query[0] == 2:
        delete_sum += d.popleft()
        rui_sum.popleft()
        continue
    # query[0] == 3:
    if query[1]-1 == 0:
        print(0)
        continue
    print(rui_sum[query[1]-1-1]-delete_sum)
    # print(rui_sum, delete_sum)
