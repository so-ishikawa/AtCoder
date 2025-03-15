#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
X = float(input())
if X >= 38.0:
    print(1)
    exit()
if X < 38.0 and X >= 37.5:
    print(2)
    exit()
print(3)
