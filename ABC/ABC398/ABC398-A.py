#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())

if N % 2 == 0:
    print("-"*((N-2)//2) + "==" + "-"*((N-2)//2))
else:
    print("-"*((N//2)) + "=" + "-"*(N//2))
