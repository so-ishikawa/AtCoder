import itertools

S, K = map(str, input().split())
K = int(K)

s = list(S)

temp = set()
for v in itertools.permutations(s):
    temp.add(v)

temp = list(temp)
temp.sort()

print("".join(list(temp[K-1])))
