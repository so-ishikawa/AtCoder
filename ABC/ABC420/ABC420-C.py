#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, Q = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

min_result = 0
for i in range(N):
    min_result = min_result + min(A_list[i], B_list[i])
# print(min_result)
for i in range(Q):
    c, X, V = map(str, input().split())
    X = int(X)
    V = int(V)
    if c == "A":
        # A_list[X-1] 
        min_result = min_result - min(A_list[X-1],B_list[X-1])
        min_result = min_result + min(V, B_list[X-1])
        A_list[X-1] = V
        print(min_result)
        continue
    min_result = min_result - min(A_list[X-1],B_list[X-1])
    min_result = min_result + min(A_list[X-1], V)
    B_list[X-1] = V
    print(min_result)
    continue
