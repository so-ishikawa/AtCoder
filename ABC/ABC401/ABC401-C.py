#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, K = map(int, input().split())

result = [1]*(N+1)

if N < K:
    print(1)
    exit()

for i in range(K, N+1):
    temp = 0
    for j in range(i-K, i):
        temp += result[j]
    result[i] = temp
print(result[N]%(10**9))
        
