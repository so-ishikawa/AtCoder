H, W = map(int, input().split())
ban = []
for _ in range(H):
    ban.append(input())

info_list = []
for _ in range(H):
    info_list.append([0]*W)

for h in range(H):
    for w in range(W):
        if ban[h][w] == "#":
            info_list[h][w] = "#"
            continue
        count = 0
        if h - 1 >= 0 and w - 1 >= 0 and ban[h-1][w-1] == "#":
            count += 1
        if h - 1 >= 0                and ban[h-1][w  ] == "#":
            count += 1
        if h - 1 >= 0 and w + 1 <= W-1 and ban[h-1][w+1] == "#":
            count += 1
        if                w - 1 >= 0 and ban[h][w-1] == "#":
            count += 1
        if                w + 1 <= W-1 and ban[h][w+1] == "#":
            count += 1
        if h + 1 <= H-1 and w - 1 >= 0 and ban[h+1][w-1] == "#":
            count += 1
        if h + 1 <= H-1 and                ban[h+1][w] == "#":
            count += 1
        if h + 1 <= H-1 and w + 1 <= W-1 and ban[h+1][w+1] == "#":
            count += 1
        info_list[h][w] = count

for h in range(H):
    for w in range(W):
        print(info_list[h][w], end="")
    print("")
            
            

