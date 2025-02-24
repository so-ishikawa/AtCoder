#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())

def f(n, value):
    if n == 1:
        print(value)
        exit()
    f(n-1, n*value)

f(N, 1)
