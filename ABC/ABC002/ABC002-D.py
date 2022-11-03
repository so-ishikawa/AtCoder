from itertools import combinations

N, M = map(int, input().split())
xy_list = []
for i in range(M):
    x, y = map(int, input().split())
    xy_list.append({x, y})

# N is person num
# M is relationship num

all_combinations = []
for all_person_num in range(N, 2-1, -1):
    temp = list(combinations(list(range(1, N+1)), all_person_num))
    all_combinations += temp

flag = False
for target_combination in all_combinations:
    pair_tuple_list = list(combinations(target_combination, 2))
    pair_set_list = [set(x) for x in pair_tuple_list]
    for pair_num in range(len(pair_set_list)):
        if pair_set_list[pair_num] not in xy_list:
            break
        if pair_num == len(pair_set_list)-1:
            flag = True
    if flag:
        print(len(target_combination))
        break
if not flag:
    print(1)
