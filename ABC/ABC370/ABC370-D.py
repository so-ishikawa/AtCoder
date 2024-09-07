H, W, Q = map(int, input().split())
# RC_list = []
masu = []
masu.append([None]*(W+2))
for i in range(H):
    temp = [1]*W
    temp.insert(0, None)
    temp.append(None)
    masu.append(temp)

masu.append([None]*(W+2))

for i in range(Q):
    # for i in masu:
    #     print(i)

    r, c = map(int, input().split())
    # RC_list.append((r, c))
    if masu[r][c] == 1:
        masu[r][c] = 0
        continue
    temp_r = r
    temp_c = c
    while True:
        temp_r = temp_r - 1
        if masu[temp_r][temp_c] == None:
            break
        if masu[temp_r][temp_c] == 0:
            continue
        masu[temp_r][temp_c] = 0
        break
        
    temp_r = r
    temp_c = c
    while True:
        temp_r = temp_r + 1
        if masu[temp_r][temp_c] == None:
            break
        if masu[temp_r][temp_c] == 0:
            continue
        masu[temp_r][temp_c] = 0
        break

    temp_r = r
    temp_c = c
    while True:
        temp_c = temp_c - 1
        if masu[temp_r][temp_c] == None:
            break
        if masu[temp_r][temp_c] == 0:
            continue
        masu[temp_r][temp_c] = 0
        break

    temp_r = r
    temp_c = c
    while True:
        temp_c = temp_c + 1
        if masu[temp_r][temp_c] == None:
            break
        if masu[temp_r][temp_c] == 0:
            continue
        masu[temp_r][temp_c] = 0
        break



_count = 0
for i in masu:
    _count += i.count(1)
    # print(i)
print(_count)
