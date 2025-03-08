#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
B_list = list(map(int, input().split()))
W_list = list(map(int, input().split()))

B_list.sort(reverse=True)
W_list.sort(reverse=True)

B_plus = [x for x in B_list if x >= 0]
W_plus = [x for x in W_list if x >= 0]
B_minus = [x for x in B_list if x < 0]
W_minus = [x for x in W_list if x < 0]

B_plus.sort(reverse=True)
W_plus.sort(reverse=True)
B_minus.sort(reverse=True)
W_minus.sort(reverse=True)

if len(B_plus) > len(W_plus):
    print(sum(B_plus)+sum(W_plus))
    exit()
elif len(B_plus) == len(W_plus):
    print(sum(B_plus)+sum(W_plus))
    exit()
elif len(B_plus) < len(W_plus):
    sum_value = 0
    temp = 0
    for i in range(min(len(W_plus), len(B_list))):
        temp += (B_list[i]+W_list[i])
        # temp = sum(B_list[:i]) + sum(W_list[:i])
        if sum_value < temp:
            sum_value = temp
    print(sum_value)
