H, W = map(int, input().split())
G_list = []
for _ in range(H):
    # G_list.append(list(str, input().split()))
    G_list.append(list(input()))
current = (0, 0)
passed_set = set({current})

dic = dict({"U":(-1, 0), "D":(1, 0), "L":(0, -1), "R":(0, 1)})



while True:
    y, x = current
    dy, dx = dic[G_list[y][x]]

    if (y+dy, x+dx) in passed_set:
        print(-1)
        exit()
    if y+dy<0 or y+dy>=H or x+dx<0 or x+dx>=W:
        break
    current = (y+dy, x+dx)
    passed_set.add(current)

    """
    # print(current, passed_set)
    y, x = current
    # print(G_list[0][0])
    if G_list[y][x] == "U":
        if (y-1, x) in passed_set:
            print(-1)
            exit()
        if y-1 < 0:
            break
        current = (y-1, x)
        passed_set.add(current)
        continue

    if G_list[y][x] == "D":
        if (y+1, x) in passed_set:
            print(-1)
            exit()
        if y+1 >= H:
            break
        current = (y+1, x)
        passed_set.add(current)
        continue

    if G_list[y][x] == "L":
        if (y, x-1) in passed_set:
            print(-1)
            exit()
        if x-1 < 0:
            break
        current = (y, x-1)
        passed_set.add(current)
        continue

    if G_list[y][x] == "R":
        # print("hello!")
        if (y, x+1) in passed_set:
            print(-1)
            exit()
        if x+1 >= W:
            break
        current = (y, x+1)
        passed_set.add(current)
        continue
    """
print(current[0]+1, current[1]+1)
