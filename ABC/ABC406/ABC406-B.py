#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, K = map(int, input().split())
A_list = list(map(int, input().split()))

temp = 1
for i in A_list:
    if temp*i > (10**K-1):
        temp = 1
        continue
    temp = temp * i
print(temp)
