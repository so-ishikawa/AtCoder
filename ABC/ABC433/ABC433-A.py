#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
X, Y, Z = map(int, input().split())

for i in range(1000):
    if X == Z*Y:
        print("Yes")
        exit()
    X += 1
    Y += 1
print("No")
