#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
temp = 0
for i in range(N):
    P, Q = map(int, input().split())
    temp += (Q/P)
print(temp)
