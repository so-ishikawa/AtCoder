import itertools

N = int(input())
Mg = int(input())
set_G = set()
for i in range(Mg):
    u, v = map(int, input().split())
    set_G.add((min(u,v), max(u,v)))
Mh = int(input())
set_H = set()
for i in range(Mh):
    a, b = map(int, input().split())
    set_H.add((min(a,b), max(a,b)))

value_dic = dict()
for i in range(1, N):
    value_list = list(map(int, input().split()))
    for j in range(i+1,N+1):
        temp = value_list.pop(0)
        value_dic[(i,j)] = temp

min_cost = 999999999999999999999999999999999
for i in itertools.permutations(range(1, N+1)):
    score = 0
    trans_dic = dict()
    for j in range(len(i)):
        trans_dic[j+1] = i[j]

    new_set = set()

    for j in set_G:
        v_h = (min(trans_dic[j[0]], trans_dic[j[1]]), max(trans_dic[j[0]], trans_dic[j[1]]))
        new_set.add(v_h)

    make_set = new_set - set_H
    delete_set = set_H - new_set

    for j in make_set:
        score += value_dic[j]
    for j in delete_set:
        score += value_dic[j]

    if min_cost > score:
        min_cost = score

print(min_cost)
