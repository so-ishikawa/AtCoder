N, K = map(int, input().split())
A_list = list(map(int, input().split()))

XY_list = []
for i in range(N):
    x, y = map(int, input().split())
    XY_list.append((x, y))

XY_list.insert(0, "dummy")
light_position_list = []
illuminated_position_list = []

for i in range(len(XY_list)):
    if i == 0:
        continue
    if i in A_list:
        light_position_list.append(XY_list[i])
        continue
    illuminated_position_list.append(XY_list[i])


