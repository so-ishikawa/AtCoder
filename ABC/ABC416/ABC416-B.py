#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = input()

T = S
T = list(T)

for i in range(len(T)-1, -1, -1):
    if T[i] == ".":
        T[i] = "o"
        break

for i in range(len(T)):
    if T[i] == "o":
        break

    if T[i] != "#":
        continue

    if i == 0:
        continue

    if T[i-1] == "#":
        continue

    T[i-1] = "o"

print("".join(T))        
