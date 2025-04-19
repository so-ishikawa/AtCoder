#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

temp = ""
S = input()
for i in S:
    if i.isupper():
        temp += i
print(temp)
