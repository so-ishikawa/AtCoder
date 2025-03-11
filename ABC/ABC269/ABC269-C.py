#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())

for i in range(N+1):
    if N == N | i:
        print(i)
