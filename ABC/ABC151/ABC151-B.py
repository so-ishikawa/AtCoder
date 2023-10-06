N, K, M = map(int, input().split())
A_list = list(map(int, input().split()))

target_score_sum = N * M
temp = target_score_sum - sum(A_list)

if temp > K:
    print(-1)
    exit()
if temp < 0:
    print(0)
    exit()
print(temp)
