#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M = map(int, input().split())
A_list = list(map(int, input().split()))



diff = len(A_list) - M

max_value = 0
for d in range(diff+1):
    temp = 0
    for i in range(M):
        temp += (i+1)*A_list[i+d]

    max_value = max(max_value, temp)
print(max_value)
