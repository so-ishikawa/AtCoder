#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N = int(input())
dic = dict()
for i in range(1, N+1):
    S = input()
    dic[i] = S
X, Y  = map(str, input().split())
X = int(X)

if dic[X] == Y:
    print("Yes")
    exit()

print("No")
