H, W, N = map(int, input().split())
T = input()
S_list = []
for _ in range(H):
    S = input()
    S_list.append(S)

dic = {"L":(0, -1), "R":(0, 1), "U":(-1, 0), "D":(1, 0)}
T_result = None
temp = [0, 0] #diff
for t in T:
    h, w = dic[t]
    temp[0] = temp[0] + h
    temp[1] = temp[1] + w

count = 0

for h in range(H):
    for w in range(W):
        if h == 0 or h == H-1 or w == 0 or w == W-1:
            continue
        if h + temp[0] < 0 or h + temp[0] > H-1:
            continue
        if w + temp[1] < 0 or w + temp[1] > W-1:
            continue
        if S_list[h][w] == "#":
            continue
        # ---------
        current_h = h
        current_w = w
        flag = True
        for t in T:
            temp_h, temp_w = dic[t]
            current_h += temp_h
            current_w += temp_w
            if current_h < 0 or current_h > H-1:
                flag = False
                break
            if current_w < 0 or current_w > W-1:
                flag = False
                break
            if S_list[current_h][current_w] == "#":
                flag = False
                break
        if flag:
            count += 1
print(count)
