#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))

temp = set()

for a in A_list:
    if a == -1:
        continue
    if a in temp:
        print("No")
        exit()
    temp.add(a)
print("Yes")

remain = set(range(1, N+1)) - temp
remain = list(remain)

for i in A_list:
    if i != -1:
        print(i, end=" ")
        continue
    t = remain.pop()
    print(t, end=" ")

