#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, Q = map(int, input().split())
A_list = list(map(int, input().split()))

for _ in range(Q):
    B = int(input())
    if max(A_list) < B:
        print(-1)
        continue
    temp = 0
    for a in A_list:
        if B - 1 >= a:
            temp += a
            continue
        temp += (B-1)
    print(temp+1)
