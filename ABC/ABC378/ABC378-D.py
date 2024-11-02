H, W, K = map(int, input().split())
S_list = []
for _ in range(H):
    s = input()
    S_list.append(s)

count = 0

def f(_count, ban, current):
    global count
    # print("hello", _count, ban, current, S_list)
    if _count == K:
        count += 1
        # print(ban)
        return
    h, w = current
    if h-1>=0 and S_list[h-1][w] == "." and ban[h-1][w]:
        ban[h-1][w] = False
        f(_count+1, ban, (h-1, w))
        ban[h-1][w] = True
    if h+1<H and S_list[h+1][w] == "." and ban[h+1][w]:
        ban[h+1][w] = False
        f(_count+1, ban, (h+1, w))
        ban[h+1][w] = True
    if w-1>=0 and S_list[h][w-1] == "." and ban[h][w-1]:
        ban[h][w-1] = False
        f(_count+1, ban, (h, w-1))
        ban[h][w-1] = True
    if w+1<W and S_list[h][w+1] == "." and ban[h][w+1]:
        ban[h][w+1] = False
        f(_count+1, ban, (h, w+1))
        ban[h][w+1] = True
    
        
for h in range(H):
    for w in range(W):
        if S_list[h][w] == "#":
            continue
        start = (h, w)
        ban = []
        for _h in range(H):
            ban.append([True]*W)

        ban[h][w] = False
        _count = 0
        f(_count, ban, start)

print(count)
