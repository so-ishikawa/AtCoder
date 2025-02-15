#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = input()
count = 0

for i in range(len(S)):
    if S[i] != "A":
        continue
    for j in range(i, len(S)):
        if S[j] != "B":
            continue
        diff = j - i
        if j+diff < len(S) and S[j+diff] == "C":
            count += 1

print(count)
