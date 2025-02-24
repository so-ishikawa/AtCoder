#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())

temp = [True]*(N+1)

temp[0] = False
temp[1] = False

for i in range(2, N+1):
    if temp[i] is False:
        continue
    count = 2
    while i*count <= N:
        temp[i*count] = False
        count += 1

for i in range(len(temp)):
    if not temp[i]:
        continue
    print(i, end=" ")
