#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import collections

N = int(input())
A_list = list(map(int, input().split()))

c = collections.Counter(A_list)

result = 0
momo = dict()
for i in list(c.keys()):
    for j in list(c.keys()):
        if i == j:
            continue
        if (min(i,j),max(i,j)) in momo:
            continue
        momo[(min(i,j),max(i,j))] = ""
        result += c[i]*c[j]*(i*i - 2*i*j + j*j)
print(result)
