A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

if S + T >= K:
    print(S*A + B*T - (S+T)*C)
    exit()
print(S*A + T*B)
