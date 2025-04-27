#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import bisect
N, M = map(int, input().split())
dic = dict()

for i in range(1, M+1):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)):
        if temp[j] in dic:
            dic[temp[j]].add(i)
            continue
        dic[temp[j]] = set({i})

B_list = list(map(int, input().split()))
B_list.insert(0, "dummy")

# all_dish = set(range(1, M+1))

last_day_list = [None]*(M+1)

for day in range(N, 0, -1):
    # print(day, "!")
    b = B_list[day]
    if b not in dic:
        continue
    for i in dic[b]:
        if last_day_list[i] is not None:
            continue
        last_day_list[i] = day    
    # all_dish = all_dish - dic[b]

last_day_list.pop(0)
last_day_list.sort()

result = []
for i in range(1, N+1):
    temp = bisect.bisect(last_day_list, i)
    print(temp)

