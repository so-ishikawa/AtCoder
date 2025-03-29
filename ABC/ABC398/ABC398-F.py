#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = input()

if len(S) == 1:
    print(S)
    exit()
if len(S) == 2:
    if S[0] == S[1]:
        print(S)
        exit()
    print(S+S[0])
    exit()





_S = S[::-1]

no = -1
for i in range(1, len(_S)):
    if _S[0] != _S[i]:
        no = i
        break
print(S + _S[no:])
