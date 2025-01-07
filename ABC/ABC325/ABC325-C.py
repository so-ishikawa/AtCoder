H, W = map(int, input().split())
S_list = []
for i in range(H):
    S_list.append(input())

sensors_heads_set = set()
sensor_HW = list()
for i in range(H):
    sensor_HW.append([None]*W)

for h in range(H):
    for w in range(W):
        if S_list[h][w] != "#":
            continue
        temp = None
        if h-1>=0 and w-1>=0 and S_list[h-1][w-1] == "#":
            temp = (h-1, w-1)
        if h-1>=0 and S_list[h-1][w] == "#":
            temp = (h-1, w)
        if h-1>=0 and w+1<W and S_list[h-1][w+1] == "#":
            temp = (h-1, w+1)
        if w-1>=0 and S_list[h][w-1] == "#":
            temp = (h, w-1)
        if w+1<W and S_list[h][w+1] == "#":
            temp = (h, w+1)
        if h+1<H and w-1>=0 and S_list[h+1][w-1] == "#":
            temp = (h+1, w-1)
        if h+1<H and S_list[h+1][w] == "#":
            temp = (h+1, w)
        if h+1<H and w+1<W and S_list[h+1][w+1] == "#":
            temp = (h+1, w+1)

        if temp is None:
            sensor_HW[h][w] = True
            sensors_heads_set.add((h,w))
            continue

        if sensor_HW[temp[0]][temp[1]] == None:
            pass
        else:
            while sensor_HW[temp[0]][temp[1]] != True:
                temp = sensor_HW[temp[0]][temp[1]]

        if (h, w) > temp:
            sensor_HW[h][w] = temp
            if temp not in sensors_heads_set:
                sensors_heads_set.add(temp)
            sensor_HW[temp[0]][temp[1]] = True
            continue
        else:
            sensor_HW[h][w] = True
            sensor_HW[temp[0]][temp[1]] = (h,w)
            sensors_heads_set.discard(temp)
            sensors_heads_set.add((h,w))

print(len(sensors_heads_set))
print(sensors_heads_set)
