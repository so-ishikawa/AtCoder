import sys

sys.setrecursionlimit(20000000)


H, W = map(int, input().split())
S_list = []
S = None
G = None
for i in range(H):
    temp = input()
    if "S" in temp:
        S = (i, temp.index("S"))
    if "G" in temp:
        G = (i, temp.index("G"))
    S_list.append(temp)


min_count = 9999999999999999999

def f(last_vertical, count, pass_set, current):
    global min_count
    # print(last_vertical, count, pass_set, current)
    if current == G:
        if min_count > count:
            min_count = count
        return
    if last_vertical:
        x_r = current[1]+1
        x_l = current[1]-1
        y = current[0]
        if x_r < W:
            next_right = (y, x_r)
            if next_right not in pass_set and S_list[y][x_r] != "#":
                temp = pass_set.copy()
                temp.add((next_right))
                f(not last_vertical, count+1, temp, next_right)

        if x_l >= 0:
            next_left = (y, x_l)
            if next_left not in pass_set and S_list[y][x_l] != "#":
                temp = pass_set.copy()
                temp.add(next_left)
                f(not last_vertical, count+1, temp, next_left)
        # return
    # tate
    else:
        y_d = current[0]+1
        y_u = current[0]-1
        x = current[1]
        if y_d < H:
            next_down = (y_d, x)
            if next_down not in pass_set and S_list[y_d][x] != "#":
                temp = pass_set.copy()
                temp.add(next_down)
                f(not last_vertical, count+1, temp, next_down)

        if y_u >= 0:
            next_up = (y_u, x)
            if next_up not in pass_set and S_list[y_u][x] != "#":
                temp = pass_set.copy()
                temp.add(next_up)
                f(not last_vertical, count+1, temp, next_up)

    

if S[0]-1 >= 0 and S_list[S[0]-1][S[1]] != "#":
    f(True, 1, set({S, (S[0]-1, S[1])}), (S[0]-1, S[1]))

if S[0]+1 < H and S_list[S[0]+1][S[1]] != "#":
    f(True, 1, set({S, (S[0]+1, S[1])}), (S[0]+1, S[1]))

if S[1]-1 >= 0 and S_list[S[0]][S[1]-1] != "#":
    f(False, 1, set({S, (S[0], S[1]-1)}), (S[0], S[1]-1))

if S[1]+1 < W and S_list[S[0]][S[1]+1] != "#":
    f(False, 1, set({S, (S[0], S[1]+1)}), (S[0], S[1]+1))


if min_count ==  9999999999999999999:
    print(-1)
    exit()
print(min_count)
