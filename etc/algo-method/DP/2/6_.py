N = int(input())
A_list = []

for i in range(N):
    temp = list(map(int, input().split()))
    A_list.append(temp)

masu = []
for i in range(N):
    masu.append([0]*N)

for h in range(N):
    for w in range(N):
        upper = 0
        left = 0
        if h-1>=0:
            upper = masu[h-1][w]
        if w-1>=0:
            left = masu[h][w-1]
        masu[h][w] = A_list[h][w] + max(upper, left)

print(masu[N-1][N-1])
