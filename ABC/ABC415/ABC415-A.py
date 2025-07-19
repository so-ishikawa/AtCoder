#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N = int(input())
A_set = set(map(int, input().split()))
X = int(input())

if X in A_set:
    print("Yes")
    exit()

print("No")
