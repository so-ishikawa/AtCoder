#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
for i in range(1, N+1):
    if i<= M:
        print("OK")
        continue
    print("Too Many Requests")
