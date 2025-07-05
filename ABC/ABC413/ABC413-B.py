#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
check_set = set()

N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        temp = S_list[i] + S_list[j]
        check_set.add(temp)
print(len(check_set))
        
