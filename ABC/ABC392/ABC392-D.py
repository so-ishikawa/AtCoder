#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import itertools
#import collections

N = int(input())
K_list = []
for i in range(N):
    temp = list(map(int, input().split()))
    temp.pop(0)
    K_list.append(temp)

l = list(range(N))
max_ = 0
for v in itertools.combinations(l, 2):
    a, b = v
    temp = list(set(K_list[a]) & set(K_list[b]))
    if len(temp) == 0:
        continue
    m = len(K_list[a])*len(K_list[b])

    


    
    inner_sum = 0
    for j in temp:
        inner_sum += (K_list[a].count(j) * K_list[b].count(j))
    max_ = max(max_, inner_sum/m)
print(max_)
    
