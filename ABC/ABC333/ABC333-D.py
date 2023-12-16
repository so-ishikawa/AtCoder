N = int(input())
dic = dict()
leaf_temp_list = []
leaf_set = set()
for _ in range(N-1):
    u, v = map(int, input().split())
    if u in dic:
        dic[u].append(v)
    else:
        dic[u] = [v]
    if v in dic:
        dic[v].append(u)
    else:
        dic[v] = [u]
    leaf_temp_list.append(u)
    leaf_temp_list.append(v)

for i in range(1, N+1):
    if leaf_temp_list.count(i) == 1:
        leaf_set.add(i)


min_value = 999999

def f(current_target, sum_value):
    
    global min_value
    if current_target in leaf_set:
        if min_value > sum_value:
            min_value = sum_value + 1
            return
    temp_value = 0
    print(current_target, "!!")
    for i in dic[current_target]:
        if i in leaf_set:
            temp_value += 1
    sum_value = sum_value + temp_value + 1
    if len(dic[current_target]) == temp_value:
        if min_value > sum_value:
            min_value = sum_value
            return
    for i in dic[current_target]:
        if i in leaf_set:
            continue
        f(i, sum_value)

f(1, 0)

print(min_value)
