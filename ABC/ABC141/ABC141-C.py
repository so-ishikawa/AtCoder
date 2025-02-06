#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, K, Q = map(int, input().split())
scores = [0]*N
scores.insert(0, -999999999)

for _ in range(Q):
    A = int(input())
    scores[A] = scores[A] + 1

scores.pop(0)
scores = [K - (Q - x) for x in scores]

for i in scores:
    if i > 0:
        print("Yes")
        continue
    print("No")

