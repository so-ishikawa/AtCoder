#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, A, B  = map(int, input().split())
S = list(input())

S = S[A:]
S.reverse()
S = S[B:]
S.reverse()
print("".join(S))

