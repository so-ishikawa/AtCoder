#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())

S_move = ""
T_move = ""

for i in range(M):
    S, A = map(str, input().split())
    A = int(A)
    S_move += (S*A)
for i in range(L):
    T, B = map(str, input().split())
    B = int(B)
    T_move += (T*B)

Sr = Rt
Sc = Ct
Tr = Ra
Tc = Ca
count = 0
# print(Sr, Sc, Tr, Tc)
for index in range(N):
    s = S_move[index]
    if s == "U":
        Sr = Sr - 1
    if s == "D":
        Sr = Sr + 1
    if s == "L":
        Sc = Sc - 1
    if s == "R":
        Sc = Sc + 1

    t = T_move[index]
    if t == "U":
        Tr = Tr - 1
    if t == "D":
        Tr = Tr + 1
    if t == "L":
        Tc = Tc - 1
    if t == "R":
        Tc = Tc + 1
    # print(Sr, Sc, Tr, Tc)
    if Sr == Tr and Sc == Tc:
        count += 1
print(count)
