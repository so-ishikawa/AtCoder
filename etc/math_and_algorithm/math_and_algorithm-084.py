#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

a,b,c = map(int, input().split())
if c-a-b < 0:
    print("No")
    exit()
if 4*a*b < (c-a-b)**2:
    print("Yes")
    exit()
print("No")
