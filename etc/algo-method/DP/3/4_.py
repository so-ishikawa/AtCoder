N, M = map(int, input().split())
W_list = list(map(int, input().split()))
V_list = list(map(int, input().split()))

masu = []
for _ in range(N+1):
    masu.append([-1]*(M+1))

masu[0][0] = 0

for n in range(N+1):
    if n == N:
        break
    for m in range(M+1):
        if masu[n][m] == -1:
            continue

        masu[n+1][m] = max(masu[n+1][m], masu[n][m])

        if m+W_list[n]>M:
            continue

        masu[n+1][m+W_list[n]] = max(masu[n+1][m+W_list[n]], masu[n][m] + V_list[n])
# print(masu)
print(max(masu[N]))
        
