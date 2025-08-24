#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
Q = int(input())
tenp = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        tenp.append(x)
    else:
        print(min(tenp))
        tenp.remove(min(tenp))
        
