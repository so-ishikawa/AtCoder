#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, Q = map(int, input().split())
temp = []
for i in range(1, N+1):
    temp.append(i)

top_index = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        p = q[1] - 1
        x = q[2]
        temp[(top_index + p) % N] = x
        continue
    elif q[0] == 2:
        p = q[1] - 1
        print(temp[(top_index + p) % N])
        continue
    else:
        #q[0] == 3:
        k = q[1]
        top_index = (top_index + k) % N
        
