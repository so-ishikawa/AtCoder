N = int(input())

S_list = []
for i in range(N):
    S_list.append(input())

masu = []
for i in range(N):
    masu.append([0]*N)

masu[0][0] = 1

for h in range(N):
    for w in range(N):
        if h == 0 and w == 0:
            continue
        if S_list[h][w] == "#":
            continue
        temp = 0
        if h-1>=0 and S_list[h-1][w]!="#":
            temp += masu[h-1][w]
        if w-1>=0 and S_list[h][w-1]!="#":
            temp += masu[h][w-1]
        masu[h][w] = temp

print(masu[N-1][N-1])
