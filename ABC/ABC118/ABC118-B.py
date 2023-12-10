N, M = map(int, input().split())

temp = set(range(1, M+1))

for _ in range(N):
    k_list = list(map(int, input().split()))
    k_list.pop(0)
    temp = temp & set(k_list)

print(len(temp))
