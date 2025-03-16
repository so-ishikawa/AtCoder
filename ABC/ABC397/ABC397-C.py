#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N = int(input())
A_list = list(map(int, input().split()))
A_sum_set_list = [0]*len(A_list)
A_flag_list = [True]*(N+1)

temp_A = 0
for i in range(len(A_list)):
    a = A_list[i]
    if A_flag_list[a]:
        temp_A += 1
        A_flag_list[a] = False
    A_sum_set_list[i] = temp_A
    
# print(A_sum_set_list)
B_list = list(reversed(A_list))
B_sum_set_list = [0]*len(B_list)
B_flag_list = [True]*(N+1)

temp_B = 0
for i in range(len(B_list)):
    a = B_list[i]
    if B_flag_list[a]:
        temp_B += 1
        B_flag_list[a] = False
    B_sum_set_list[i] = temp_B
    
B_sum_set_list.reverse()

max_value = 0
for i in range(len(A_sum_set_list)-1):
    temp = A_sum_set_list[i] + B_sum_set_list[i+1]
    max_value = max(max_value, temp)
print(max_value)
