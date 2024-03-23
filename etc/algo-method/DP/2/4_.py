N = int(input())

masu = []
for i in range(N):
    masu.append([0]*N)

masu[0][0] = 1

for h in range(N):
    for w in range(N):
        if h == 0 and w == 0:
            continue
        temp = 0
        if h-1>=0:
            temp += masu[h-1][w]
        if w-1>=0:
            temp += masu[h][w-1]
        masu[h][w] = temp

print(masu[N-1][N-1])
