s = int(input())
position_list = []
for i in range(s):
    N, M = map(int, input().split())
    position_list.append((N, M))

# position_list.sort()

key_list = []
for i in range(len(position_list)-1):
    x = position_list[i+1][0] - position_list[i][0]
    y = position_list[i+1][1] - position_list[i][1]
    key_list.append((x, y))
# print(key_list)
s_ = int(input()) 
picture_list = []
for i in range(s_):
    N, M = map(int, input().split())
    picture_list.append((N, M))

check_set = set(picture_list)

for point in picture_list:
    flag = True
    temp_point = point
    for key_ in key_list:
        temp_point = (temp_point[0] + key_[0], temp_point[1] + key_[1])
        # print(temp_point)
        if temp_point not in check_set:
            flag = False
            break
    if flag:
        print(point[0]-position_list[0][0], point[1]-position_list[0][1])
        break
