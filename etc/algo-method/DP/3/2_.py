N, M = map(int, input().split())
W_list = list(map(int, input().split()))

masu = []
for i in range(N+1):
    masu.append([False]*(M+1))

masu[0][0] = True

for h in range(N+1):
    if h == N:
        break
    for w in range(M+1):
        if not masu[h][w]:
            continue
        masu[h+1][w] = True
        if w + W_list[h] <= M:
            masu[h+1][w+W_list[h]] = True

print("Yes" if masu[N][M] else "No") 
