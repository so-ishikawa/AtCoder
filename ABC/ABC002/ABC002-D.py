N, M = map(int, input().split())
xy_list = []
for i in range(M):
    x, y = map(int, input().split())
    xy_list.append({x, y})

# N is person num
# M is relationship num

each_person_relationship_list = {}
for n in range(1, N+1):
    temp = []
    for _n in range(1, N+1):
        if n == _n:
            continue
        if {n, _n} in xy_list:
            temp.append(_n)
    each_person_relationship_list[n] = temp

max_group_num = 0
for n in range(1, N+1):
    temp = each_person_relationship_list[n]
    if temp == []:
        continue
    base_set = set(each_person_relationship_list[temp[0]])
    for i in temp:
        base_set = base_set & set(each_person_relationship_list[i])
    print(n, base_set)
    # if max_group_num < len(base_set) + 1:
    #     max_group_num = len(base_set) + 1
    #print(max_group_num)
