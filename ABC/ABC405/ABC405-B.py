#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
A_list = list(map(int, input().split()))

check_set = set()
count = 0

#0 case
temp = set(A_list)
if len(temp) != M:
    print(0)
    exit()

for i in A_list:
    if i not in check_set and i <= M:
        check_set.add(i)
    count += 1
    if len(check_set) == M:
        break
print(N-count+1)
