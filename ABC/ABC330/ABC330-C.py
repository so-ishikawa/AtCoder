import math
import bisect
D = int(input())

sqrt_x_list = [x*x for x in range(0, math.ceil(math.sqrt(D))+1)]

min_value = 9999999999999999999

for x2 in sqrt_x_list:
    index = bisect.bisect(sqrt_x_list, D-x2)
    lhs = 999999999999999999999
    rhs = 999999999999999999999
    if index != 0:
        lhs = abs(D - (sqrt_x_list[index-1] + x2))
    if index != len(sqrt_x_list):
        rhs = abs(D - (sqrt_x_list[index] + x2))
    min_value = min(min_value, lhs, rhs)
print(min_value)
