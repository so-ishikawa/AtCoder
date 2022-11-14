"""
# 方針
残りの数の最小値 ←→　選んだ数の最大値で考える
"""

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

sum_value = sum(A_list)

dic = {}
for i in A_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_value = 0

for i in A_list:
    num = i
    temp_value = i*dic[i]
    while (num+1)%M in dic:
        num = (num+1)%M
        temp_value = temp_value + (num*dic[num])

    max_value = max(temp_value, max_value)

print(sum_value - max_value)

