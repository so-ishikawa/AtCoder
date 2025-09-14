#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

X, Y = map(int, input().split())

def f(x):
    x = str(x)
    # x = x.reverse()
    x = list(x)
    x.reverse()
    x = "".join(x)
    return(int(x))

a1 = X
a2 = Y
count = 0
while True:
    temp = f(a2+a1)
    a1 = a2
    a2 = temp
    # print(a2)
    if count > 6:
        break
    count+= 1
print(a2)
