#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

A1,A2,A3 = map(int, input().split())
temp = [A1, A2, A3]
temp.sort()

if temp[0]*temp[1] == temp[2]:
    print("Yes")
    exit()
print("No")
