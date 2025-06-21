#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
D_list = list(map(int, input().split()))

sum_ = 0
real = []

for i in range(len(D_list)):
    #
    #print(D_list[i])
    sum_ = sum_ + D_list[i]
    real.append(sum_)

for i in real:
    print(i, end=" ")
print("")

s_temp = real.copy()
temp = []
while True:
    if len(s_temp) == 1:
        break
    first = 0
    for i in range(len(s_temp)):
        if i == 0:
            first = s_temp[i]
            continue
        temp.append(s_temp[i] - first)
    for i in temp:
        print(i, end= " ")
    print("")
    s_temp.clear()
    s_temp = temp.copy()
    temp.clear()

    
