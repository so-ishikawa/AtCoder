#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
skill_set = set()
skill_list = []
for i in range(1, N+1):
    a, b = map(int, input().split())
    if a == b == 0:
        skill_set.add(i)
        continue
    skill_list.append((i, a, b))

for i in skill_list:
    num, a, b = i
    
    if a not in skill_set and b not in skill_set:
        continue
    # if a in skill_set and b in skill_set:
    #     continue
    skill_set.add(num)
    # skill_set.add(b)
print(len(skill_set))
