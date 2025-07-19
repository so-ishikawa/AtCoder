#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

S = input()

left_posi = -1
for i in range(len(S)):
    if S[i] == ".":
        continue
    if left_posi == -1:
        left_posi = i + 1
        continue
    print(str(left_posi)+","+str(i+1))
    left_posi = -1

    
    
