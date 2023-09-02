import bisect
N, D, P = map(int, input().split())
F_list = list(map(int, input().split()))

F_list.sort()
temp = P / D
lower_days = bisect.bisect(F_list, temp)
over_days = len(F_list) - lower_days
sum_remain_days = sum(F_list[:lower_days])


if over_days == 0:
    print(sum(F_list))
    exit()

if over_days % D == 0:    
    print(sum_remain_days + (over_days//D)*P)
    exit()


# tsukaikiru
use_days = (over_days // D)*D
non_use_days = len(F_list) - use_days
tukaikiru = (sum(F_list[:non_use_days]) + (use_days//D)*P)

#amaru
amaru = sum_remain_days + ((over_days // D) + 1)*P
print(min(tukaikiru, amaru))
# print(tukaikiru, amaru)
