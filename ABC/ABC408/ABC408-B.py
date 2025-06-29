#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_set = set(map(int, input().split()))
temp = list(A_set)
temp.sort()

print(len(temp))
for i in temp:
    print(i, end = " ")
