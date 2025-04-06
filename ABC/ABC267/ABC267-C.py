#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M = map(int, input().split())
A_list = list(map(int, input().split()))
A_list.insert(0, "dummy")

S = 0
for i in range(1, M+1):
    S += i*A_list[i]
max_value = S

if N == M:
    print(max_value)
    exit()

T = 0
for i in range(1, M+1):
    T += A_list[i]
S = S - T + M*A_list[M+1]
# print(S)
max_value = max(max_value, S)


for n in range(3, N+1):
    if N < n-1+M:
        break
    T = T - A_list[n-2] + A_list[n-2+M]
    S = S -T + M*A_list[n-1+M]

    max_value = max(max_value, S)
print(max_value)
