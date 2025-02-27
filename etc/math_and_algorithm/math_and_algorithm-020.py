#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

N = int(input())
A_list = list(map(int, input().split()))

A_list.sort()
count = 0
for a in range(len(A_list)-4):
    for b in range(a+1, len(A_list)-3):
        for c in range(b+1, len(A_list)-2):
            for d in range(c+1, len(A_list)-1):
                for e in range(d+1, len(A_list)):
                    if A_list[a] + A_list[b] + A_list[c] + A_list[d] + A_list[e] > 1000:
                        break
                    if A_list[a] + A_list[b] + A_list[c] + A_list[d] + A_list[e] == 1000:
                        count += 1
print(count)
