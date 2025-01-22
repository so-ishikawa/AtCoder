import itertools

N, M = map(int, input().split())

l = list(range(1, M+1))
result = set()
for v in itertools.permutations(l, N):
    temp = list(v)
    temp.sort()
    result.add(tuple(temp))
result = list(result)
result.sort()

for i in result:
    print(*i)
