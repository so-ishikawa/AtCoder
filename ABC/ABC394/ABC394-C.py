#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = input()
temp = ""
result = ""

for s in S:
    if temp != "":
        if s == "W":
            temp += s
            continue
        if s == "A":
            temp += "A"
            C_len = len(temp) -1
            result += ("A" + "C"* C_len)
            temp = ""
            continue
        else:
            temp += s
            result += temp
            temp = ""
            continue
    else:
        if s == "W":
            temp += s
            continue
        else:
            result += s
            continue
if temp != "":
    result += temp
print(result)
