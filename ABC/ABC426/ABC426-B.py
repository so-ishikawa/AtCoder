#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = input()

temp = set(S)
temp = list(temp)

if S.count(temp[0]) == 1:
    print(temp[0])
    exit()
print(temp[1])
    
