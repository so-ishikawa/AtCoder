#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
A_list = list(map(int, input().split()))

if M >= sum(A_list):
    print("Yes")
    exit()
print("No")
