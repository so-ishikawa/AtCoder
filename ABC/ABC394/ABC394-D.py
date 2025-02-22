#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
from collections import deque

S = input()
d = deque()
for s in S:
    if s == ")":
        if len(d) != 0 and d[-1] == "(":
            d.pop()
            continue
    if s == "]":
        if len(d) != 0 and d[-1] == "[":
            d.pop()
            continue
    if s == ">":
        if len(d) != 0 and d[-1] == "<":
            d.pop()
            continue
    d.append(s)

if len(d) == 0:
    print("Yes")
    exit()
print("No")
