#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
A, B, C, D = map(int, input().split())

if A < C:
    print("No")
    exit()
if A > C:
    print("Yes")
    exit()
# A == C
if B < D:
    print("No")
    exit()
print("Yes")
