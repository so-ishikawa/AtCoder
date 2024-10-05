import itertools
import math

N = int(input())
K_list = list(map(int, input().split()))

target_value = math.ceil(sum(K_list)/2)
temp_value = 9999999999999999999999999999999999
for i in range(1, N+1):
    for pair in itertools.combinations(K_list, i):
        _sum = 0
        #for j in pair:
        #     _sum += K_list[j]
        _sum = sum(pair)
        if _sum >= target_value and temp_value > _sum:
            temp_value = _sum
print(temp_value)
