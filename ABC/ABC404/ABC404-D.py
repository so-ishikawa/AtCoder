#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M = map(int, input().split())
C_list = list(map(int, input().split()))

A_list = []
for i in range(M):
    A = list(map(int, input().split()))
    A.pop(0)
    A_list.append(A)


