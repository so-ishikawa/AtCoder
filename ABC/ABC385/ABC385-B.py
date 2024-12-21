H, W, X, Y = map(int, input().split())
S_list = []
for i in range(H):
    S = input()
    S_list.append(S)
T = input()

passed_list = []
for i in range(H):
    passed_list.append([None]*W)

y = X-1
x = Y-1
house_count = 0

for i in T:
    # print(i)
    if i == "U":
        if y - 1 < 0 or S_list[y-1][x] == "#":
            continue
        if S_list[y-1][x] == "@" and passed_list[y-1][x] is None:
            house_count += 1
            passed_list[y-1][x] = True
        y = y - 1
        continue
        """
        if x - 1 < 0 or S_list[y][x-1] == "#":
            continue
        if S_list[y][x-1] == "@" and passed_list[y][x-1] is None:
            house_count += 1
            passed_list[y][x-1] = True
        x = x - 1
        continue
        """
    if i == "D":
        if y + 1 >= H or S_list[y+1][x] == "#":
            continue
        if S_list[y+1][x] == "@" and passed_list[y+1][x] is None:
            house_count += 1
            passed_list[y+1][x] = True
        y = y + 1
        continue
        """
        if x + 1 >= H or S_list[y][x+1] == "#":
            continue
        if S_list[y][x+1] == "@" and passed_list[y][x+1] is None:
            house_count += 1
            passed_list[y][x+1] = True
        x = x + 1
        continue
        """
    if i == "L":
        if x - 1 < 0 or S_list[y][x-1] == "#":
            continue
        if S_list[y][x-1] == "@" and passed_list[y][x-1] is None:
            house_count += 1
            passed_list[y][x-1] = True
        x = x - 1
        continue
        """
        if y - 1 < 0 or S_list[y-1][x] == "#":
            continue
        if S_list[y-1][x] == "@" and passed_list[y-1][x] is None:
            house_count += 1
            passed_list[y-1][x] = True
        y = y - 1
        continue
        """
    if i == "R":
        if x + 1 >= W or S_list[y][x+1] == "#":
            continue
        if S_list[y][x+1] == "@" and passed_list[y][x+1] is None:
            house_count += 1
            passed_list[y][x+1] = True
        x = x + 1
        continue
        """
        if y + 1 >= W or S_list[y+1][x] == "#":
            continue
        if S_list[y+1][x] == "@" and passed_list[y+1][x] is None:
            house_count += 1
            passed_list[y+1][x] = True
        y = y + 1
        continue
        """
    else:
        continue
print(y+1,x+1, house_count)
