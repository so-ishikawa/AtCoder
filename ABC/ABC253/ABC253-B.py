H, W = map(int, input().split())
S_list = []

for _ in range(H):
    S_list.append(input())

start = None
goal = None

for i in range(H):
    flag = False
    for j in range(W):
        if S_list[i][j] == "o":
            if start is None:
                start = (i, j)
                continue
            goal = (i, j)
            flag = True
            break
    if flag:
        break

print(abs(start[0]-goal[0])+abs(start[1]-goal[1]))

