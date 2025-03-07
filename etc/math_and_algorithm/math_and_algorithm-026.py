#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())

temp = 0

for i in range(1, N+1):
    temp += (1/i)
print(N*temp)
