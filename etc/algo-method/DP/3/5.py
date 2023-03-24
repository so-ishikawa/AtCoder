N, M = map(int, input().split())
w_list = list(map(int, input().split()))

masu = []
for i in range(N+1):
    masu.append([999999999]*(M+1))

masu[0][0] = 0

for n in range(N):
    for m in range(M+1):
        masu[n+1][m] = min(masu[n][m], masu[n+1][m])

        if w_list[n] + m > M:
            continue

        masu[n+1][m+w_list[n]] = min(masu[n+1][m+w_list[n]], masu[n][m] + 1)

# for i in masu:
#     print(i)
print(-1 if min([x[-1] for x in masu]) == 999999999 else min([x[-1] for x in masu])) 
