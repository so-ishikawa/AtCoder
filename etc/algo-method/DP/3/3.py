N,M = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

masu = []
for i in range(N):
    masu.append([-1] * M)

masu[0][0] = 0

for n in range(N):
    for m in range(M):
        if masu[n][m] < 0:
            continue
        if n + 1 <= N - 1:
            masu[n+1][m] = max(masu[n+1][m],masu[n][m])
        if (n + 1 <= N - 1) and (m + a_list[n] <= M - 1):
            masu[n+1][m+a_list[n]] = max(masu[n+1][m+a_list[n]], masu[n][m]+b_list[n])
print(masu[N-1][M-1])          
# print(masu)    
