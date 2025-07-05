#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
T = int(input())
for i in range(T):
    N = int(input())
    A_list = list(map(int, input().split()))
    if N == 2:
        print("Yes")
        continue

    A_list.sort()
    flag = True
    for j in range(2, N):
        if A_list[j]*A_list[j-2] != A_list[j-1]**2:
            flag = False
            break
    if flag:
        print("Yes")
        continue

    A_list.sort(key=abs)
    flag = True
    for j in range(2, N):
        if A_list[j]*A_list[j-2] != A_list[j-1]**2:
            flag = False
            break
    if flag:
        print("Yes")
        continue
    print("No")
