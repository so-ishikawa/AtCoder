#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = input()

world = int(S[0])
stage = int(S[-1])

if stage == 8:
    print(str(world + 1)+"-"+"1")
    exit()
print(str(world)+"-"+str(stage+1))
