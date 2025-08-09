#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
S = input()
if len(S) < 3:
    print("No")
    exit()
if S[-1] == "a" and S[-2] == "e" and S[-3] == "t":
    print("Yes")
    exit()
print("No")
