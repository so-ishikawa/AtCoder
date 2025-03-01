#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))

flag = False
for i in range(len(A_list)-1):
    if A_list[i] < A_list[i+1]:
        continue
    print("No")
    exit()
print("Yes")
