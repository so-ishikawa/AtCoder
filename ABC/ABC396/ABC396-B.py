#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
from collections import deque

d = deque([0]*100)
Q = int(input())

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        d.append(query[1])
        continue
    #query[0] == 2
    print(d.pop())
