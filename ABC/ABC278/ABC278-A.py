N, K = map(int, input().split())
A_list = list(map(int, input().split()))

for i in range(K):
    A_list.pop(0)
    A_list.append(0)

for i in A_list:
    print(i, end=" ")
