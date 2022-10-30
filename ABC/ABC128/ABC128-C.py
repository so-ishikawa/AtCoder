"""
N, M = map(int, input().split())

s_list = []
for i in range(M):
    s = list(map(int, input().split()))
    s.pop(0)
    s_list.append(s)

p_list = list(map(int, input().split()))
"""

from itertools import product

switch_pattern_list = []
all = product([True, False], repeat=4)
for i in all:
    switch_pattern_list.append(list(i))
print(switch_pattern_list)
