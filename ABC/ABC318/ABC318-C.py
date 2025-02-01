import bisect
N, D, P = map(int, input().split())

# 7 1 6 3 6
F_list = list(map(int, input().split()))
F_list.sort()

index = bisect.bisect(F_list, P/D)
over_num = len(F_list) - index

if over_num == 0:
    print(sum(F_list))
    exit()

set_num = over_num // D
temp = 9999999999999999999999999999
if set_num == 0:
    temp = sum(F_list)
else:
    temp = sum(F_list[:-1*set_num*D]) + set_num*P
set_num = set_num + 1
temp2 = sum(F_list[:-1*set_num*D]) + set_num*P
print(min(temp, temp2))


