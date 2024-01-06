N = int(input())

grid = []
for i in range(N):
    temp = [None]*N
    grid.append(temp)

grid[(N+1)//2 -1][(N+1)//2-1] = "T"

current_dir = dict({1:(0,1), 2:(1,0), 3:(0,-1), 4:(-1,0)})
next_dir = dict({1:2,2:3,3:4,4:1})

now_dir = 1
current_posi = (0, 0)
for i in range(1, N*N):
    grid[current_posi[0]][current_posi[1]] = i
    y, x = current_dir[now_dir]
    if current_posi[0]+y == N or current_posi[1]+x == N or grid[current_posi[0]+y][current_posi[1]+x] is not None:
        now_dir = next_dir[now_dir]
        y, x = current_dir[now_dir]
    current_posi = (current_posi[0]+y, current_posi[1]+x)

for i in range(N):
    for j in range(N):
        print(grid[i][j], end=" ")
    print("")
