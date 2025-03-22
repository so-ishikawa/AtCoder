#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
A1, A2, A3, A4, A5, A6, A7 = map(int, input().split())
A_list = [A1,A2,A3,A4,A5,A6,A7]
A_list.sort()

temp = set({A1,A2,A3,A4,A5,A6,A7})
temp_list = list(temp)
temp_list.sort()

if len(temp) == 1:
    print("No")
    exit()
if len(temp) == 2:
    if A_list.count(temp_list[0]) == 5 and A_list.count(temp_list[1]) == 2 \
       or A_list.count(temp_list[0]) == 2 and A_list.count(temp_list[1]) == 5:
        print("Yes")
        exit()
    if A_list.count(temp_list[0]) == 4 and A_list.count(temp_list[1]) == 3 \
       or A_list.count(temp_list[0]) == 3 and A_list.count(temp_list[1]) == 4:
        print("Yes")
        exit()
    print("No")
    exit()
if len(temp) == 3:
    if A_list.count(temp_list[0]) == 4 and A_list.count(temp_list[1]) == 2 and A_list.count(temp_list[2]) == 1 \
       or A_list.count(temp_list[0]) == 4 and A_list.count(temp_list[1]) == 1 and A_list.count(temp_list[2]) == 2 \
       or A_list.count(temp_list[0]) == 2 and A_list.count(temp_list[1]) == 4 and A_list.count(temp_list[2]) == 1 \
       or A_list.count(temp_list[0]) == 2 and A_list.count(temp_list[1]) == 1 and A_list.count(temp_list[2]) == 4 \
       or A_list.count(temp_list[0]) == 1 and A_list.count(temp_list[1]) == 4 and A_list.count(temp_list[2]) == 2 \
       or A_list.count(temp_list[0]) == 1 and A_list.count(temp_list[1]) == 2 and A_list.count(temp_list[2]) == 4:
        print("Yes")
        exit()
    
    if A_list.count(temp_list[0]) == 3 and A_list.count(temp_list[1]) == 2 and A_list.count(temp_list[2]) == 2 \
       or A_list.count(temp_list[0]) == 2 and A_list.count(temp_list[1]) == 3 and A_list.count(temp_list[2]) == 2 \
       or A_list.count(temp_list[0]) == 2 and A_list.count(temp_list[1]) == 2 and A_list.count(temp_list[2]) == 3:
        print("Yes")
        exit()

    if A_list.count(temp_list[0]) == 3 and A_list.count(temp_list[1]) == 3 and A_list.count(temp_list[2]) == 1 \
       or A_list.count(temp_list[0]) == 3 and A_list.count(temp_list[1]) == 1 and A_list.count(temp_list[2]) == 3 \
       or A_list.count(temp_list[0]) == 1 and A_list.count(temp_list[1]) == 3 and A_list.count(temp_list[2]) == 3:
        print("Yes")
        exit()

    print("No")
    exit()

if len(temp) == 4:
    if A_list.count(temp_list[0]) == 3 and A_list.count(temp_list[1]) == 2 and A_list.count(temp_list[2]) == 1 and A_list.count(temp_list[3]) == 1 \
       or A_list.count(temp_list[0]) == 3 and A_list.count(temp_list[1]) == 1 and A_list.count(temp_list[2]) == 2 and A_list.count(temp_list[3]) == 1 \
       or A_list.count(temp_list[0]) == 3 and A_list.count(temp_list[1]) == 1 and A_list.count(temp_list[2]) == 1 and A_list.count(temp_list[3]) == 2 \
       or A_list.count(temp_list[0]) == 1 and A_list.count(temp_list[1]) == 3 and A_list.count(temp_list[2]) == 2 and A_list.count(temp_list[3]) == 1 \
       or A_list.count(temp_list[0]) == 1 and A_list.count(temp_list[1]) == 3 and A_list.count(temp_list[2]) == 1 and A_list.count(temp_list[3]) == 2 \
       or A_list.count(temp_list[0]) == 1 and A_list.count(temp_list[1]) == 1 and A_list.count(temp_list[2]) == 3 and A_list.count(temp_list[3]) == 2 \
       or A_list.count(temp_list[0]) == 1 and A_list.count(temp_list[1]) == 1 and A_list.count(temp_list[2]) == 2 and A_list.count(temp_list[3]) == 3 \
       or A_list.count(temp_list[0]) == 1 and A_list.count(temp_list[1]) == 2 and A_list.count(temp_list[2]) == 1 and A_list.count(temp_list[3]) == 3 \
       or A_list.count(temp_list[0]) == 2 and A_list.count(temp_list[1]) == 1 and A_list.count(temp_list[2]) == 1 and A_list.count(temp_list[3]) == 3 \
       or A_list.count(temp_list[0]) == 1 and A_list.count(temp_list[1]) == 2 and A_list.count(temp_list[2]) == 3 and A_list.count(temp_list[3]) == 1 \
       or A_list.count(temp_list[0]) == 2 and A_list.count(temp_list[1]) == 1 and A_list.count(temp_list[2]) == 3 and A_list.count(temp_list[3]) == 1 \
       or A_list.count(temp_list[0]) == 2 and A_list.count(temp_list[1]) == 3 and A_list.count(temp_list[2]) == 1 and A_list.count(temp_list[3]) == 1:
        
       print("Yes")
       exit()

print("No")
