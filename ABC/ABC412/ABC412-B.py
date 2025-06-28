#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = input()
T = input()

for i in range(len(S)):
    if i == 0:
        continue
    if not S[i].isupper():
        continue
    if S[i-1] not in T:
        print("No")
        exit()
print("Yes")
