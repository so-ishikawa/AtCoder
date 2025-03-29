#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

T = int(input())
for _ in range(T):
    next_set = set()
    N = int(input())
    A_list = list(map(int, input().split()))
    for i in range(len(A_list)-1):
        if A_list[i] == A_list[i+1]:
            next_set.add(A_list[i])
    count = 0
    check_set = set()
    for j in range(len(A_list)-1):
        if A_list[j] in next_set or A_list[j+1] in next_set:
            continue
        if (j + 2 < 2*N and A_list[j] == A_list[j+2]) and not (j+3<2*N and A_list[j+1] == A_list[j+3]):
            continue
            
        # if (min(A_list[j], A_list[j+1]), max(A_list[j], A_list[j+1])) in check_set:
        if (A_list[j], A_list[j+1]) in check_set:
            # print((A_list[j], A_list[j+1]))
            count += 1
            # print(A_list[j], A_list[j+2])
            # print(j+2, 2*N, A_list[j])

            continue
        # check_set.add((min(A_list[j],A_list[j+1]), max(A_list[j], A_list[j+1])))
        check_set.add((A_list[j], A_list[j+1]))
        check_set.add((A_list[j+1], A_list[j]))
    # print(check_set,next_set)
    print(count)


