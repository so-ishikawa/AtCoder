N, M = map(int, input().split())
S = input()

temp = []
for _ in range(N+1+1):
    t = [9999] * (M+2)
    temp.append(t)

temp[1][0] = 0

for n in range(1, N+1+1):
    for m in range(M+1):
        if n == N+1:
            print(temp)
            # print(min([x for x in temp[n] if x != 9999]))
            exit()
        if temp[n][m] == 9999:
            continue
        s = S[n-1]
        if s == "0":
            temp[n+1][0] = min(temp[n+1][0], temp[n][m])
            continue
        if s == "1":
            if M >= m+1:
                temp[n+1][m+1] = min(temp[n+1][m+1], temp[n][m])
            temp[n+1][m] = min(temp[n+1][m], temp[n][m] + 1)
            continue
        # s == "2":
        temp[n+1][m] = min(temp[n+1][m], temp[n][m] + 1)
