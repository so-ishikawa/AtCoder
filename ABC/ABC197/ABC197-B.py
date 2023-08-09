H, W, X, Y = map(int, input().split())

S_list = []
for i in range(H):
    S_list.append(input())

X = X - 1
Y = Y - 1
can_see_num = 0
if S_list[X][Y] == ".":
    can_see_num += 1

direction = [(-1,0),(1,0),(0,1),(0,-1)]

for i in direction:
    for j in range(1, 100):
        _X = X + j*i[0]
        _Y = Y + j*i[1]
        if _X < 0 or _X >= H or _Y < 0 or _Y >= W:
            break
        if S_list[_X][_Y] == "#":
            break
        # print(_X, _Y)
        can_see_num += 1
print(can_see_num)
