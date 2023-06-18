import itertools
N, M = map(int, input().split())
a_list = []
for i in range(M):
    a = list(map(int, input().split()))
    a_list.append(a)

pairs = itertools.combinations(list(range(1, N+1)), 2)
temp = set()

for pair in pairs:
    if pair[0] > pair[1]:
        temp.add((pair[1], pair[0]))
        continue
    temp.add(pair)
    

for i in a_list:
    for j in range(len(i)-1):
        if i[j] > i[j+1]:
            temp.discard((i[j+1], i[j]))
            continue
        temp.discard((i[j], i[j+1]))

print(len(temp))
