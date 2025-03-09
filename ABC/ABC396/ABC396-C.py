#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
B_list = list(map(int, input().split()))
W_list = list(map(int, input().split()))

B_list.sort(reverse=True)
W_list.sort(reverse=True)

B_plus = len([x for x in B_list if x >= 0])
W_plus = len([x for x in W_list if x >= 0])

if B_plus >= W_plus:
    print(sum(B_list[:B_plus])+sum(W_list[:W_plus]))
    exit()
else:
    # len(B_plus) < len(W_plus):
    temp = sum(B_list[:B_plus]) + sum(W_list[:B_plus])
    sum_value = temp
    for i in range(B_plus, min(W_plus, N)):
        temp += (B_list[i]+W_list[i])
        if sum_value < temp:
            sum_value = temp
    print(sum_value)
