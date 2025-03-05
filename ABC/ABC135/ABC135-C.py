#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

count = 0
temp = A_list[-1]
for i in range(len(B_list)-1, -1, -1):
    b = B_list[i]

    if temp > b:
        count += b
        temp = A_list[i]
        # print("A")
        continue
    if temp == b:
        count += temp
        temp = A_list[i]
        # print("B")
        continue
    else:
        # temp < b
        b = abs(temp-b)
        count += temp
        temp = A_list[i]
        if temp > b:
            count += b
            temp = temp - b
            # print("C")
            continue
        if temp == b:
            count += b
            temp = 0
            # print("D")
            continue
        else:
            # _temp < b
            count += temp
            temp = 0
            # print("E")
            continue
print(count)
    
    
    
