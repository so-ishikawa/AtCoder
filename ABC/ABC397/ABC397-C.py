#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

from collections import Counter

N = int(input())
A_list = list(map(int, input().split()))

check_dic = dict()
for i in range(len(A_list)):
    a = A_list[i]
    check_dic.setdefault(a, []).append(i)


anster_list = [0]*N

keys = [k for k, v in check_dic.items() if len(v) >= 2]

for i in keys:
    temp = check_dic[i]
    _min = min(temp)
    _max = max(temp)
    for j in range(_min, _max):
        anster_list[j] = anster_list[j] + 1


m = (-1, -1)
for i in range(len(anster_list)):
    if anster_list[i] > m[1]:
        m = (i, anster_list[i])

index = m[0]+1
pre = len(set(A_list[:index]))
aft = len(set(A_list[index:]))

print(pre+aft)
