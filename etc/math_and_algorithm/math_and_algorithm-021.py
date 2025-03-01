#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

n, r = map(int, input().split())

def get_p(num, r):
    temp = 1
    for i in range(r):
        temp *= num
        num -= 1
    return(temp)

def get_c(r):
    temp = 1
    for i in range(1, r+1):
        temp *= i
    return(temp)

print(get_p(n, r)//get_c(r))
    
