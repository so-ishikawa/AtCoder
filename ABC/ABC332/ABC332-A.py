N, S, K = map(int, input().split())
PQ_list = []
temp = 0
for _ in range(N):
    p, q = map(int, input().split())
    temp = temp + p * q

if temp >= S:
    print(temp)
    exit()
print(temp + K)
