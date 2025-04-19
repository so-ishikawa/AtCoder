#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

N, M = map(int, input().split())
dic = dict()

for i in range(M):
    A, B = map(int, input().split())

    A = A
    B = B
    if (A+B)%N in dic:
        dic[(A+B)%N] = dic[(A+B)%N] + 1
    else:
        dic[(A+B)%N] = 1

all = M*(M-1)//2

for i in dic.values():
    if i == 1:
        continue
    all -= i*(i-1)//2
print(all)
