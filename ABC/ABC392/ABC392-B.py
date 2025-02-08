#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

all_set = set(range(1, N+1))
temp = all_set - set(A_list)
temp = list(temp)
temp.sort()

print(len(temp))
print(*temp)
