#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M = map(int, input().split())
A_list = list(map(int, input().split()))
A_list.insert(0, "dummy")

S = 0
for i in range(1, M+1):
    S += i*A_list[i]
T = 0
for i in range(1, M+1):
    T += A_list[i]
max_value = S
# print(S, T)
for i in range(2, N+1):
    if i-1+M > N:
        break
    # if i > 2:
    
    S = S - T + M * A_list[i-1+M]
    T = T - A_list[i-1] + A_list[i-1+M]
    # print(S, T)
    max_value = max(max_value, S)
print(S)
