#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, K = map(int, input().split())

result = [1]*(N+1)

if N < K:
    print(1)
    exit()
temp = K
for i in range(K, N+1):
    if i == K:
        result[i] = K
        continue
    temp = temp + result[i-1] - result[i-1-K]
    result[i] = temp%(10**9)
print(result[N])
        
