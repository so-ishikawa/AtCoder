"""
# 方針
A_listの最大値 < M　が重要
A_listの最大値 +1 == Mのケースを考慮する必要がある
"""

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()

temp = []
previous_value = -1

for i in A_list:
    if temp == []:
        temp.append([i])
    else:
        if previous_value + 1 == i or previous_value == i:
            temp[len(temp)-1].append(i)
        else:
            temp.append([i])
    previous_value = i

temp_sum = [sum(x) for x in temp]

if A_list[len(A_list)-1] + 1 == M and A_list[0] == 0 and len(temp_sum) != 1:
    temp_sum[len(temp_sum)-1] += temp_sum[0]
print(sum(A_list) - max(temp_sum))

