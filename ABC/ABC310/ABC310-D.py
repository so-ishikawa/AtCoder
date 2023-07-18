import math
N, T, M = map(int, input().split())
dic = dict()

for _ in range(M):
    a, b = map(int, input().split())
    if a in dic:
        dic[a].add(b)
    else:
        dic[a] = set({b})
    if b in dic:
        dic[b].add(a)
    else:
        dic[b] = set({a})

hater_persons_set = set(dic.keys())
hater_persons_list = list(hater_persons_set)
friendly_person_list = list(set(range(1, N+1)) - hater_persons_set)

# print(hater_persons_set, hater_persons_list, friendly_person_list)

team_list = []
for _ in range(T):
    team_list.append(set())

count = 0
# print(team_list)
def f(_team_list, person_index):
    # print(_team_list)
    global count
    if person_index == N - 1:
        if _team_list.count(set()) == 0:
            count += 1
        return
    
    if person_index >= len(hater_persons_list):
        # friendly
        friendly_person_index = person_index - len(hater_persons_list)
        # print(friendly_person_index)
        for i in range(T):
            _team_list_copy_ = _team_list.copy()
            _team_list_copy_[i].add(friendly_person_list[friendly_person_index])
            f(_team_list_copy_, person_index+1)
        return

    for i in range(len(_team_list)):
        if dic[hater_persons_list[person_index]] & _team_list[i] != set():
            continue
        _team_list_copy = _team_list.copy()
        _team_list_copy[i].add(hater_persons_list[person_index])
        f(_team_list_copy, person_index+1)

f(team_list.copy(), 0)
print(count)
