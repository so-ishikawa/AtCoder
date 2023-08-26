N, M = map(int, input().split())

to_dic = dict()

dis_dic = dict()

for i in range(M):
    a, b, c = map(int, input().split())
    if a in to_dic:
        to_dic[a].append(b)
    else:
        to_dic[a] = [b]
    if b in to_dic:
        to_dic[b].append(a)
    else:
        to_dic[b] = [a]

    dis_dic[(a, b)] = c
    dis_dic[(b, a)] = c

max_length = 0

pass_city = [False]*(N+1)

def f(city_num, current_length):
    global max_length
    pass_city[city_num] = True
    for i in to_dic[city_num]:
        if pass_city[i]:
            continue
        f(i, current_length + dis_dic[(city_num, i)])
    pass_city[city_num] = False
    if max_length < current_length:
        max_length = current_length

for i in range(1, N+1):
    if i not in to_dic:
        continue
    f(i, 0)

print(max_length)
