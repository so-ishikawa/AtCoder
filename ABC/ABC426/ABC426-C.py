#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, Q = map(int, input().split())
# XY_list = []

sum_list = []
sum_list.append("dummy")
for i in range(1, N+1):
    sum_list.append(i)

last_value = -1
for i in range(Q):
    X, Y = map(int, input().split())

    if last_value > X:
        print(0)
        continue

    last_value = X
    print(sum_list[X])
    for j in range(X+1, Y):
        sum_list[j] = sum_list[j] - sum_list[X]


