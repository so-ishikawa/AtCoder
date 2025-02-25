#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

N = int(input())

set_ = set()

for i in range(1, int(math.sqrt(N))+1):
    if N % i != 0:
        continue
    set_.add(N//i)
    set_.add(i)

for i in set_:
    print(i)
