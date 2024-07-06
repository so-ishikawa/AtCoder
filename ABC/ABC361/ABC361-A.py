N, K, X = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.insert(K, X)
print(*A_list)
