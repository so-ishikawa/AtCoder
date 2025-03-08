#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int,input().split()))

count = 0

for i in range(N-2):
    if A_list[i] == A_list[i+1] == A_list[i+2]:
        print("Yes")
        exit()
print("No")
