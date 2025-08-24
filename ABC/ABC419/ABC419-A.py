#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

S = input()
dic = dict()
dic["red"] = "SSS"
dic["blue"] = "FFF"
dic["green"] = "MMM"

if S in dic:
    print(dic[S])
    exit()
print("Unknown")
