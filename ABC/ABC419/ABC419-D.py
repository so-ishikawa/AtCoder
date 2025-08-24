#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M = map(int, input().split())
S = input()
T = input()
temp = [True] * N
for _ in range(M):
    L, R = map(int, input().split())
    for i in range(L-1, R):
        temp[i] = not temp[i]

for i in range(N):
    if temp[i]:
        print(S[i], end="")
        continue
    print(T[i],end="")
