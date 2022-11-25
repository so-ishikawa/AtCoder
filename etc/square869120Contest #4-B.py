"""
方針
ビルをグループ単位に分ける ※この時点でK<=G_numなら解決
グループとはそれまでの左から最高の高さから次の最高を更新するまでのビル群
グループの左端のやつを頭と呼称しグループ内で非頭で頭との差分を配列として持っておく
差分が少ない　→　増築するだけの費用が低いと考える
最後に左からグループの頭を列挙し頭同士で同じ高さなら+1する処理でその合計の費用を出す

"""
N, K = map(int, input().split())
a_list = list(map(int, input().split()))


GROUP_TOP = 999999999
total_cost = 0

# N 建物数
# K 見えてほしい数
group_list = [0] * N
highest = 0
for i in range(N):
    if highest <= a_list[i]:
        group_list[i] = GROUP_TOP
        highest = a_list[i]

group_top_hight = 0
for i in range(N):
    if group_list[i] == GROUP_TOP:
        group_top_hight = a_list[i]
        continue
    group_list[i] = group_top_hight - a_list[i]


while group_list.count(GROUP_TOP) < K:
    min_cost = min(group_list)
    min_cost_index = group_list.index(min_cost)

    total_cost += min_cost
    group_list[min_cost_index] = GROUP_TOP
    a_list[min_cost_index] += min_cost
    for i in range(min_cost_index+1, N):
        if group_list[i] == GROUP_TOP:
            break
        group_list[i] = a_list[min_cost_index] - a_list[i]


pre_group_top_hight = a_list[0]
for i in range(1, N):
    if group_list[i] != GROUP_TOP:
        continue

    if pre_group_top_hight >= a_list[i]:
        temp = pre_group_top_hight - a_list[i] + 1
        a_list[i] += temp
        total_cost += temp
    pre_group_top_hight = a_list[i]

print(total_cost)

