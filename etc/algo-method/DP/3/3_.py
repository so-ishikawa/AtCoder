N, M = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

masu = []
for _ in range(N):
    masu.append([-1]*M)

masu[0][0] = 0

for n in range(N):
    for m in range(M):
        if masu[n][m] == -1:
            continue
        if n+1 <= N-1:
            masu[n+1][m] = max(masu[n+1][m], masu[n][m])
            if m+A_list[n] <= M-1:
                masu[n+1][m+A_list[n]] = max(masu[n+1][m+A_list[n]], masu[n][m]+B_list[n])

if not masu[N-1][M-1]:
    print(-1)
    exit()
# print(masu)
print(masu[N-1][M-1])
