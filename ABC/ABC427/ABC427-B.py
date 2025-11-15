#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

def f(_int):
    _str = str(_int)
    temp = 0
    for s in _str:
        temp += int(s)
    return temp

N = int(input())

dic = dict()
dic[0] = 1

def ff(i):
    if i == 0:
        return 1
    if i in dic:
        return(dic[i])

    temp = 0
    for j in range(i):
        temp += f(ff(j))
    if i not in dic:
        dic[i] = temp
    return(temp)

print(ff(N))
