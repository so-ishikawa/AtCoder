#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

import numpy as np

N = int(input())
S_list = []
T_list = []
for i in range(N):
    s = list(input())
    S_list.append(s)
for i in range(N):
    t = list(input())
    T_list.append(t)

min_diff = 9999999999999999999999999999999999
for i in range(0, 3+1):
    temp = np.rot90(S_list, -1*i)
    # print(temp)
    count = 0
    for j in range(N):
        for k in range(N):
            # print(j, k)
            if T_list[j][k] != temp[j][k]:
                count += 1
    if min_diff > count + i:
        min_diff = count + i
print(min_diff)

