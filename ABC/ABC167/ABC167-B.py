A, B, C, K = map(int, input().split())

if A >= K:
    print(K)
    exit()
if A + B >= K:
    print(A)
    exit()

print(A + (-1*(K - (A+B))))

