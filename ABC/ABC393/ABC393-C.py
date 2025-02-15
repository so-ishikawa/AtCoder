#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())

temp_set = set()

for i in range(M):
    u, v = map(int, input().split())
    temp_set.add((min(u,v), max(u,v)))

aaa = temp_set.copy()

for i in temp_set:
    u, v = i
    if u == v:
        aaa.discard(i)

print(M-len(aaa))
