N = int(input())
A_list = []

for i in range(N):
    temp = list(map(int, input().split()))
    temp.reverse()
    A_list.append(temp)

masu = []
for i in range(N):
    masu.append([0]*N)

masu[0][0] = A_list[0][0]

for h in range(N):
    for w in range(N):
        if h == 0 and w == 0:
            continue
        upper = 99999999
        left = 99999999
        if h-1>=0:
            upper = masu[h-1][w]
        if w-1>=0:
            left = masu[h][w-1]
        masu[h][w] = A_list[h][w] + min(upper, left)

print(masu[N-1][N-1])
