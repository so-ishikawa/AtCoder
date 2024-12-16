N = int(input())
A_list = []
B_list = []
for i in range(N):
    A = list(input())
    A_list.append(A)

for i in range(N):
    B_list.append([""]*N)

# print(B_list)
for y in range(N):
    for x in range(N):
        c = (min(x, y, N-x-1, N-y-1)+1) % 4

        ny = y
        nx = x
        for _ in range(c%4):
            ty = nx
            tx = N - 1 - ny
            ny = ty
            nx = tx
        B_list[ny][nx] = A_list[y][x]


for y in range(N):
    for x in range(N):
        print(B_list[y][x], end="")
    print("")

