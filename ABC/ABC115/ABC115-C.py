#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
from collections import deque
N, K = map(int, input().split())

d = deque()

h_list = []

for i in range(N):
    h_list.append(int(input()))

h_list.sort()

for i in range(K):
    d.append(h_list[i])

min_ = d[-1] - d[0]

for i in range(K, N):
    d.popleft()
    d.append(h_list[i])
    min_ = min(min_, d[-1]-d[0])

print(min_)
