N, M = map(int, input().split())
A_list = list(map(int, input().split()))

masu = []
for n in range(N):
    masu.append([False]*M)

masu[0][0] = True

for h in range(N):
    if h == N-1:
        break
    for w in range(M):
        if not masu[h][w]:
            continue
        masu[h+1][w] = True
        if w+A_list[h] < M:
            masu[h+1][w+A_list[h]] = True
print(masu[N-1].count(True))
