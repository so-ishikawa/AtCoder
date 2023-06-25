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

max_all_light_length = 0
for i in illuminated_position_list:
    min_each_light_length = 999999999999999
    for j in light_position_list:
        temp_min = ((i[0] - j[0])**2 + (i[1] - j[1])**2)**(1/2)
        # print(temp_min)
        if temp_min < min_each_light_length:
            min_each_light_length = temp_min
    if max_all_light_length < min_each_light_length:
        max_all_light_length = min_each_light_length
print(max_all_light_length)

