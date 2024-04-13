N, M = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

masu = []
for _ in range(N):
    masu.append([None]*M)

masu[0][0] = 0

for n in range(N):
    for m in range(M):
        if masu[n][m] is None:
            continue
        if n+1 <= N-1:
            if masu[n+1][m] is not None:
                masu[n+1][m] = max(masu[n+1][m], masu[n][m])
            else:
                masu[n+1][m] = masu[n][m]
            if m+A_list[n] <= M-1:
                if masu[][]
                masu[n+1][m+A_list[n]] = max(masu[n+1][m+A_list[n]], masu[n+1][m+A_list[n]]+B_list[n])

if not masu[N-1][M-1]:
    print(-1)
    exit()

print(masu[N-1][M-1])
