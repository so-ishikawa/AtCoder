import bisect
N, M = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()

max_num = 0

for index in range(len(A_list)):
    i = A_list[index]
    temp = bisect.bisect_left(A_list, i+M)
    temp = temp - index
    if temp > max_num:
        # print(index)
        max_num = temp

print(max_num)
