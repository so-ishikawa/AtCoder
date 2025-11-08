#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, L, R = map(int, input().split())
S = input()
# print(S[L-1:R],"o" * (R - L + 1))
if S[L-1:R] == "o" * (R - L + 1):
    print("Yes")
    exit()
print("No")
