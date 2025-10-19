#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M, K = map(int, input().split())
dic = dict()

for i in range(K):
    A, B = map(int, input().split())

    if A in dic:
        dic[A].add(B)
    else:
        dic[A] = set({B})

    if len(dic[A]) == M:
        print(A, end= " ")

