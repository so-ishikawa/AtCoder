#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, S = map(int, input().split())

count = 0

for red in range(1, N+1):
    for blue in range(1, N+1):
        if red + blue > S:
            break
        count += 1
print(count)
