#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, K = map(int, input().split())
R_list = list(map(int, input().split()))

R_list.sort()

C = 0
for R in R_list[-1*K:]:
    C = (C + R)/2
print(C)
