N, M = map(int, input().split())
w_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

masu = []
for i in range(N+1):
    masu.append([-1]*(M+1))


masu[0][0] = 0

for n in range(N):
    for m in range(M+1):
        if masu[n][m] < 0:
            continue
        
        masu[n+1][m] = max(masu[n+1][m], masu[n][m])

        if (m + w_list[n]) <= (M):
            # continue
            masu[n+1][m + w_list[n]] =  max((masu[n][m] + v_list[n]), masu[n][m + w_list[n]])

print(max(masu[N]))
