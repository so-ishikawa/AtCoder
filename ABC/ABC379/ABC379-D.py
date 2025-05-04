#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
# 解説AC
from collections import deque

Q = int(input())
d = deque()
current = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        d.append(current)
        continue
    if query[0] == 2:
        current += query[1]
        continue
    else:
        #query[0] == 3
        H = query[1]
        count = 0
        while len(d) > 0 and d[0] <= current - H:
            count += 1
            d.popleft()
        print(count)
        
