import math
N = int(input())
L_list = []
R_list = []
for i in range(N):
    num, LR = map(str, input().split())
    num = int(num)
    if LR == "L":
        L_list.append(num)
        continue
    R_list.append(num)

#L_list.sort()
# R_list.sort()

sum_a = 0
for i in range(1, len(L_list)):
    sum_a += abs(L_list[i-1]-L_list[i])
sum_b = 0
for i in range(len(L_list)-1):
    sum_b += abs(L_list[i+1]-L_list[i])
min_L = min(sum_a, sum_b)

sum_a = 0
for i in range(1, len(R_list)):
    sum_a += abs(R_list[i-1]-R_list[i])
sum_b = 0
for i in range(len(R_list)-1):
    sum_b += abs(R_list[i+1]-R_list[i])
min_R = min(sum_a, sum_b)

print(min_L+min_R)




"""
min_L = sum([abs(x-L_list[0]) for x in L_list])
max_L = sum([abs(x-L_list[-1]) for x in L_list])
num_floor_L = math.floor(sum(L_list))
num_ceil_L = math.ceil(sum(L_list))
floor_L =  sum([abs(x-num_floor_L) for x in L_list])
ceil_L =  sum([abs(x-num_ceil_L) for x in L_list])
result_L = min(min_L, max_L, floor_L, ceil_L)

min_R = sum([abs(x-R_list[0]) for x in R_list])
max_R = sum([abs(x-R_list[-1]) for x in R_list])
num_floor_R = math.floor(sum(R_list))
num_ceil_R = math.ceil(sum(R_list))
floor_R =  sum([abs(x-num_floor_R) for x in R_list])
ceil_R =  sum([abs(x-num_ceil_R) for x in R_list])
result_R = min(min_R, max_R, floor_R, ceil_R)

print(result_L + result_R)
"""
