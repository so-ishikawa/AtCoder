N, K = map(int, input().split())

temp = N
for _ in range(K):
    # print(temp)
    if temp % 200 == 0:
        temp = temp // 200
        continue

    temp = temp * 1000 + 200
print(temp)
