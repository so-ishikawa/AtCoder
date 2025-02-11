#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import sys
sys.setrecursionlimit(20000000)

N = int(input())
H_list = list(map(int, input().split()))

if len(H_list) == 1:
    print("Yes")
    exit()

def f(current_index, previous_height):
    if current_index == len(H_list)-1:
        if H_list[current_index] - previous_height >= 0:
            print("Yes")
            exit()
        print("No")#, current_index, previous_height)
        exit()
    if H_list[current_index] == previous_height:
        f(current_index+1, H_list[current_index])
    elif H_list[current_index] - previous_height >= 1:
        f(current_index+1, H_list[current_index])
        f(current_index+1, H_list[current_index]-1)
    else:
        return

f(1, H_list[0])
print("No")
exit()
