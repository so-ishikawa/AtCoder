#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
from collections import deque

d = deque()

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        d.append(query[1])
        continue
    #[2]
    print(d[0])
    d.popleft()


