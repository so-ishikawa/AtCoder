#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-




def has_drug(state, k):
    return (state >> (k-1)) & 1 == 1


def f(i, passed, S, state):
    if  

    
T = int(input())
for _ in range(T):
    N = int(input())
    S = input()

    for i in range(1, N+1):
        passed = set()
        f(i, passed, S, 0)
    
