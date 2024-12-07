H, W, D = map(int, input().split())
S_list = []
for _ in range(H):
    S_list.append(input())

humid_flag = []
for h in range(H):
    humid_flag.append([False]*W)

old_humid_list = []
current_humid_list = []

for h in range(H):
    for w in range(W):
        if S_list[h][w] == "H":
            current_humid_list.append((h, w))
            humid_flag[h][w] = True

for _ in range(D):
    temp_humid_list = []
    for i in current_humid_list:
        h = i[0]
        w = i[1]
        if h+1 <= H-1 and S_list[h+1][w] == "." and humid_flag[h+1][w] == False:
            temp_humid_list.append((h+1, w))
            humid_flag[h+1][w] = True
        if h-1 >= 0 and S_list[h-1][w] == "." and humid_flag[h-1][w] == False:
            temp_humid_list.append((h-1, w))
            humid_flag[h-1][w] = True      
        if w+1 <= W-1 and S_list[h][w+1] == "." and humid_flag[h][w+1] == False:
            temp_humid_list.append((h, w+1))
            humid_flag[h][w+1] = True
        if w-1 >= 0 and S_list[h][w-1] == "." and humid_flag[h][w-1] == False:
            temp_humid_list.append((h, w-1))
            humid_flag[h][w-1] = True

    old_humid_list += current_humid_list
    current_humid_list.clear()
    current_humid_list = temp_humid_list

print(len(old_humid_list + current_humid_list))
