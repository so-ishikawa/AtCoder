A, B, K = map(int, input().split())

for i in range(999999999999):
    if A * (K**i) >= B:
        print(i)
        exit()
