#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
B_list = list(map(int, input().split()))
W_list = list(map(int, input().split()))

B_plus = [x for x in B_list if x >= 0]
W_plus = [x for x in W_list if x >= 0]
B_minus = [x for x in B_list if x < 0]
W_minus = [x for x in W_list if x < 0]

B_plus.sort(reverse=True)
W_plus.sort(reverse=True)
B_minus.sort()
W_minus.sort()

if len(B_plus) > len(W_plus):
    print(sum(B_plus)+sum(W_plus))
    exit()
elif len(B_plus) == len(W_plus):
    print(sum(B_plus)+sum(W_plus))
    exit()
elif len(B_plus) < len(W_plus):
    max_value = 0
    for i in range(len(B_plus), len(W_plus)+1):

        temp = sum(B_plus) + sum(B_minus[:i-len(B_plus)]) + sum(W_plus[:i])
        # print(i, temp)
        if max_value < temp:
            max_value = temp
    print(max_value)
