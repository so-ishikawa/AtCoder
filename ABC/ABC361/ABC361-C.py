N, K = map(int, input().split())
A_list = list(map(int, input().split()))
A_list.sort()

min_value = 9999999999999999999999999999
for _K in range(1, K+1):
    for k in range(_K):
        _min = A_list[0 + k]
        _max = A_list[-1 - (_K-k)]
        temp = _max - _min
        if min_value > temp:
            min_value = temp

print(min_value)
