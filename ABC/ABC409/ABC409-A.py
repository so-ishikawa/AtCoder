#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
T = input()
A = input()

for i in range(N):
    if T[i] == A[i] == "o":
        print("Yes")
        exit()
print("No")
