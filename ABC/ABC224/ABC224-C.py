#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import itertools

N = int(input())
XY_list = []
# Y_list = []
for _ in range(N):
    X, Y = map(int, input().split())
    XY_list.append((X, Y))
XY_list.sort()

count = 0
l = list(range(N))
for v in itertools.combinations(l, 3):
    a, b, c = v
    a = XY_list[a]
    b = XY_list[b]
    c = XY_list[c]
    
    
        count += 1
print(N-count)
  
