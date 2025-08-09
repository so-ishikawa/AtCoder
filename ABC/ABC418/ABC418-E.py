#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
XY_list = []
for _ in range(N):
    X, Y = map(int, input().split())
    XY_list.append((X, Y))

l = range(N)
count = 0
import itertools
for v in itertools.combinations(l, 4):
    a = XY_list[v[0]]
    b = XY_list[v[1]]
    c = XY_list[v[2]]
    d = XY_list[v[3]]
    if (a[0]-b[0]) != 0:
        y = (a[1]-b[1])/(a[0]-b[0])
    else:
        y = 0
    if (c[0]-d[0]) != 0:
        x = (c[1]-d[1])/(c[0]-d[0])
    else:
        x = 0
    # print(x, y)
    if abs(y) == abs(x):
        print(a,b,c,d)
        count += 1
print(count)
