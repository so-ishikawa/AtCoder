#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

import itertools

A,B,C,D = tuple(input())
A = int(A)
B = int(B)
C = int(C)
D = int(D)
l = [["+","+","+"],["+","+","-"],["+","-","+"],["+","-","-"],
     ["-","+","+"],["-","+","-"],["-","-","+"],["-","-","-"]]
# l = ["+","-"]
# for v in itertools.combinations_with_replacement(l, 3):
for v in l:
    temp = 0
    if v[0] == "+":
        temp = A + B
    else:
        temp = A - B
    if v[1] == "+":
        temp = temp + C
    else:
        temp = temp - C
    if v[2] == "+":
        temp = temp + D
    else:
        temp = temp - D
    # print(v, temp)
    if temp == 7:
        print(str(A)+v[0]+str(B)+v[1]+str(C)+v[2]+str(D)+"=7")
        exit()
