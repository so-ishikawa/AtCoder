#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

max_ = 0
temp = 0
for n in range(N-M+1):
    # temp = 0
    if n == 0:
        for i in range(M):
            temp += A_list[i]*(i+1)
        max_ = max(max_, temp)
        continue
    for i in range(n-1, n-1+M):
        temp -= A_list[i]
    temp += M*A_list[n-1+M]
    max_ = max(max_, temp)
    # print(A_list[n], A_list[n+1], A_list[n+2], A_list[n+3])
print(max_)
