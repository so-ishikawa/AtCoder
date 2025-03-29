#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
T = int(input())
for i in range(T):
    next_set = set()
    A_list = list(map(int, input().split()))
    for j in range(len(A_list)-1):
        if A_list[i] == A_list[i+1]:
            next_set.add(A_list[i])
    count = 0
    check_set = set()
    for j in range(len(A_list)-1):
        if A_list[j] in next_set or A_list[j+1] in next_set:
            continue
        if (min(A_list[i], A_list[i+1]), max(A_list[i], A_list[i+1])) in check_set:
            continue
        check_set.add((min(A_list[i],A_list[i+1]), max(A_list[i], A_list[i+1])))
        count += 1
    print(count)


