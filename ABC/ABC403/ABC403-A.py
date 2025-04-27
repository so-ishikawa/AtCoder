#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))
temp = 0
for i in range(N):
    if i % 2 == 0:
        temp += A_list[i]
print(temp)
