#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))
K = int(input())

temp = [x for x in A_list if x >= K]
print(len(temp))
