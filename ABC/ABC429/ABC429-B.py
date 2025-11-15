#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
A_list = list(map(int, input().split()))

diff = sum(A_list) - M
if diff < 0:
    print("No")
    exit()
if diff in set(A_list):
    print("Yes")
    exit()
print("No")
