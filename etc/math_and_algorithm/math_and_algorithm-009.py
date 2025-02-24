#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import itertools

N, S = map(int, input().split())
l = list(map(int, input().split()))

if S > sum(l):
    print("No")
    exit()

if S < min(l):
    print("No")
    exit()

for i in range(1, N+1):
    for v in itertools.combinations(l, i):
        if sum(v) == S:
            print("Yes")
            exit()
print("No")

