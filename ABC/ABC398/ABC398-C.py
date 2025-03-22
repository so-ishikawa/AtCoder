#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))

max_value = 0
check_list = [False]*(10**9+1)

for i in A_list:
    if check_list[i]:
        continue
    max_value = max(max_value, i)
    check_list[i] = True
