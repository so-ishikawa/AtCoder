#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = input()

group_list = []
num_list = []
pre = None
count = 0

for s_index in range(len(S)):
    s = S[s_index]
    if s_index == 0:
        count = 1
        group_list.append(s)
        pre = s
        continue
    if s == pre:
        count += 1
        continue
    # s != pre:
    num_list.append(count)
    count = 1
    pre = s
    group_list.append(s)
num_list.append(count)

sum_value = 0
for i in range(len(num_list)-1):
    min_length = min(num_list[i], num_list[i+1])
    if int(group_list[i+1]) - int(group_list[i]) == 1:
        sum_value += min_length
print(sum_value)
