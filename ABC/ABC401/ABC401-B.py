#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
state = False # logout
count = 0
for i in range(1, N+1):
    S = input()
    if S == "login":
        state = True
    if S == "logout":
        state = False
    if S == "private" and not state:
        count += 1
        
print(count)
