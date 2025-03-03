#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
temp = 0
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

for i in range(N):
    temp += (A_list[i]*(1/3) + B_list[i]*(2/3))
print(temp)
