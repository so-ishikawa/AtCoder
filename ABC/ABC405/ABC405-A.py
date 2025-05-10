#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
R, X = map(int, input().split())

if X == 1 and 1600 <= R <= 2999:
    print("Yes")
    exit()
if X == 2 and 1200 <= R <= 2399:
    print("Yes")
    exit()
print("No")
