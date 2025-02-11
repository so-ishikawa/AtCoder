#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
temp = []

for i in range(N):
    A, B = map(int, input().split())
    temp.append((A, B))

temp.sort(key=lambda x: x[0])

num = 0
cost = 0
for i in temp:
    A, B = i
    if num + B <= M:
        num += B
        cost += A*B
        continue
    cost += A*(M - num)
    break
print(cost)
