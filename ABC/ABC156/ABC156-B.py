N, K = map(int, input().split())

# temp = 0

for i in range(100):
    # temp += K**i
    if K**i > N:
        print(i)
        exit()
