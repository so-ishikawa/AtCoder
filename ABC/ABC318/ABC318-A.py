N, M, P = map(int, input().split())

if N < M:
    print(0)
    exit()

temp = N - M
print((temp//P) + 1)
