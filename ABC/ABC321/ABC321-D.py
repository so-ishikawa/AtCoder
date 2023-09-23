import bisect
N, M, P = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort()

sum_value = 0
for n in A_list:
    # for m in B_list:
    temp = [n + x for x in B_list]
    # print(temp)
    index = bisect.bisect_left(temp, P)
    sum_value = sum_value + sum(temp[:index]) + (len(temp) - index)*P
print(sum_value)
