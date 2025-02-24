#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, X, Y = map(int, input().split())

temp = set()

for i in range(1, N+1):
    if i % X == 0 or i % Y == 0:
        temp.add(i)
print(len(temp))
