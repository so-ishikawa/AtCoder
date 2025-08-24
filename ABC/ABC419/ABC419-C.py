#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
min_R = 999999999999999999999
max_R = -1
min_C = 999999999999999999999
max_C = -1
for i in range(N):
    R, C = map(int, input().split())
    min_R = min(min_R, R)
    max_R = max(max_R, R)
    min_C = min(min_C, C)
    max_C = max(max_C, C)
import math
print(math.ceil(max(max_R-min_R, max_C-min_C) / 2))
