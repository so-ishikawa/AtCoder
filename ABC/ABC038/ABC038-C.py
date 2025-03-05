#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N = int(input())
a_list = list(map(int, input().split()))
total_count = 0
current_count = 1
pre_value = a_list[0]

for i in range(1, len(a_list)):
    if pre_value < a_list[i]:
        pre_value = a_list[i]
        current_count += 1
        if i == len(a_list)-1:
            temp = current_count*(current_count-1)//2
            total_count += temp            
        continue

    if current_count > 1:
        temp = current_count*(current_count-1)//2
        total_count += temp
    pre_value = a_list[i]
    current_count = 1

print(total_count+N)
