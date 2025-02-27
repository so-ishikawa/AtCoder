#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

A, B = map(int, input().split())
setA = set()
setB = set()

for i in range(1, int(math.sqrt(A))+1):
    if A % i == 0:
        setA.add(i)
        setA.add(A//i)
for i in range(1, int(math.sqrt(B))+1):
    if B % i == 0:
        setB.add(i)
        setB.add(B//i)
print(max(setA & setB))

