import copy
import bisect
N = int(input())
A_list = list(map(int, input().split()))
sorted_A_list = A_list.copy()
sorted_A_list.sort()

bubun_wa_list = [0]*len(A_list)
temp = 0
for i in range(len(sorted_A_list)):
    bubun_wa_list[i] = temp + sorted_A_list[i]
    temp = temp + sorted_A_list[i]





# print(sorted_A_list)
# print(bubun_wa_list)
for i in A_list:
    index = bisect.bisect_right(sorted_A_list, i)
    # print(index)
    # print(bubun_wa_list[index-1])
    # """
    if index != 0:
        index = index - 1
    print(bubun_wa_list[-1] - bubun_wa_list[index], end=" ")
    # """
