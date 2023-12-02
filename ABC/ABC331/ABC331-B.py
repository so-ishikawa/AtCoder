N, S, M, L = map(int, input().split())

ans = 9999999999999999999999
for s in range(17+1):
    for m in range(13+1):
        for l in range(9+1):
            if s*6 + m*8 + l*12 >= N:
                ans = min(ans, s*S + m*M + l*L)

print(ans)
