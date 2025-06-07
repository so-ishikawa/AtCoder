#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
count = 0
X, Y = map(int, input().split())

for i in range(1, 6+1):
    for j in range(1, 6+1):
        if i + j >= X:
            count += 1
            continue
        if abs(i - j)>=Y:
            count += 1
            continue
if count == 0:
    print(0)
    exit()
print(count/36)
