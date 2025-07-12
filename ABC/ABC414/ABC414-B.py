#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
temp = ""

for i in range(N):
    c, l = map(str, input().split())
    l = int(l)
    if l > 100:
        print("Too Long")
        exit()
    temp += (c*l)
    if len(temp) > 100:
        print("Too Long")
        exit()
print(temp)
    
