#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = list(input())
T = list(input())

last_S = S[0]
last_T = T[0]

for i in range(len(S)):
    if S[i] != last_S:
        last_S = S[i]
        S[i] = "," + S[i]

for i in range(len(T)):
    if T[i] != last_T:
        last_T = T[i]
        T[i] = "," + T[i]

_S = "".join(S)
_T = "".join(T)

_S = _S.split(",")
_T = _T.split(",")

if len(_S) != len(_T):
    print("No")
    exit()
# print(_S, _T)
for i in range(len(_S)):
    if _S[i][0] != _T[i][0]:
        print("No")
        exit()
    if len(_S[i]) > len(_T[i]):
        print("No")
        exit()
    if len(_S[i]) == 1 and len(_T[i]) != 1:
        print("No")
        exit()
print("Yes")
