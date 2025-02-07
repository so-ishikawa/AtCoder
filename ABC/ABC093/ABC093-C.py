#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

A, B, C = map(int, input().split())

temp = [A, B, C]
even = [x for x in temp if x % 2 == 0]

count = 0
if not(len(even) == 3 or len(even) == 0):
    if len(even) == 1:
        for i in range(len(temp)):
            if temp[i] % 2 == 1:
                temp[i] = temp[i] + 1
    else:
        for i in range(len(temp)):
            if temp[i] % 2 == 0:
                temp[i] = temp[i] + 1
    count += 1

temp.sort(reverse=True)

count += (temp[0] - temp[1])//2
count += (temp[0] - temp[2])//2

print(count)    
