#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, L, R = map(int, input().split())
count = 0
for i in range(N):
    X, Y = map(int, input().split())
    if X <= L and R <= Y:
        count += 1
print(count)
