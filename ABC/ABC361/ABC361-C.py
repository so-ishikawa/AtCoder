N, K = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()

min_value = 99999999999999999999999
for i in range(K+1):
    # print(i+N-K-1, i)
    temp = A_list[i+N-K-1] - A_list[i]
    if min_value > temp:
        min_value = temp

print(min_value)
