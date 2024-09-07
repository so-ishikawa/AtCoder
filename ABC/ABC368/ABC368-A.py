N, K = map(int, input().split())
A_list = list(map(int, input().split()))

for i in range(K):
    temp = A_list.pop()
    A_list.insert(0,temp)

print(*A_list)