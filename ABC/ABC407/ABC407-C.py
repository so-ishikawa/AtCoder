#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = list(input())

S.reverse()

A_count = len(S)
temp_sum = 0
temp_B = 0

for s in S:
    s = int(s)
    if s < temp_B:
        s = s + 10
    temp_sum += (s - temp_B)
    temp_B = (temp_sum) % 10
    # print(temp_B)
print(A_count + temp_sum)

    
