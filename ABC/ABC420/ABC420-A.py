#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
X, Y = map(int, input().split())

if (X+Y) %12 == 0:
    print(12)
    exit()
print((X+Y)%12)
