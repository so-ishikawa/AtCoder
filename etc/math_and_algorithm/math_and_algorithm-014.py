#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

N = int(input())
result = []
n = N
for i in range(2, int(math.sqrt(N))+1):
# for i in range(2, int(N**0.5)+1):
    while n % i == 0:
        n /= i
        result.append(i)
result.append(n)
print(*result)
