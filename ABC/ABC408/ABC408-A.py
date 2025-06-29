#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, S = map(int, input().split())
T_list = list(map(int, input().split()))

if S < T_list[0]:
    print("No")
    exit()

pre = T_list[0]
for i in range(1, N):
    diff = T_list[i] - pre
    if diff > S:
        print("No")
        exit()
    pre = T_list[i]
print("Yes")
