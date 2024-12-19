# check https://atcoder.jp/contests/abc363/submissions/55870782
# import itertools
from more_itertools import distinct_permutations

N, K = map(int ,input().split())
S = input()
"""
temp = set()
for v in itertools.permutations(list(S)):
    temp.add("".join(v))
"""
temp = distinct_permutations(S)
include = 0

for T in temp:
    flag = False
    for i in range(N-K+1):
        if T[i:i+K] == T[i:i+K][::-1]:
            flag = True
            break
        
    if not flag:
        include += 1


print(include)
# print(len(temp)-include)
