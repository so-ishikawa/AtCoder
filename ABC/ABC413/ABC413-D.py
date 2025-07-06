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

    A_list.sort()
    pre = [x for x in A_list if x == A_list[0]]
    aft = [x for x in A_list if x == A_list[-1]]

    if len(pre) + len(aft) != len(A_list):
         print("No")
         continue
    temp = abs(len(pre) - len(aft))
    if (temp == 0 or temp == 1) and pre[0] == -1*aft[0]:
        print("Yes")
        continue
    print("No")
