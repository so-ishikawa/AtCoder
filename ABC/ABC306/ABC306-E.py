import bisect
N, K, Q = map(int, input().split())
XY_list = []
for i in range(Q):
    x, y = map(int, input().split())
    XY_list.append((x, y))

sorted_list = [0]*N
vis_list = [0]*N

for i in range(len(XY_list)):
    temp = vis_list[XY_list[i][0]-1]
    position = bisect.bisect(sorted_list, temp)
    sorted_list.pop(position-1)
    bisect.insort(sorted_list, XY_list[i][1])

    vis_list[XY_list[i][0]-1] = XY_list[i][1]
    
    print(sum(sorted_list[K:]))

