import itertools

N, M = map(int, input().split())
side_set = set()

for i in range(M):
    u, v = map(int, input().split())
    side_set.add((u,v))
    side_set.add((v,u))

counter = 0

check_pair = list(itertools.combinations(range(1,N+1), 3))
for pair in check_pair:
    if (pair[0], pair[1]) in side_set and (pair[1], pair[2]) in side_set and (pair[2], pair[0]) in side_set:
        counter += 1

print(counter)
