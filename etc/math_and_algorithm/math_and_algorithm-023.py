#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
B_list = list(map(int, input().split()))
R_list = list(map(int, input().split()))
print((sum(B_list)+sum(R_list))/N)
