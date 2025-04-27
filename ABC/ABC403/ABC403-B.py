#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
T = input()
U = input()

temp = [T]
check_str = list(set(U))

temp_dst = []
        
for i in range(4):
    for t in temp:
        for c in check_str:
            temp_dst.append(t.replace("?", c, 1))
    temp = []
    temp = temp_dst
    temp_dst = []

for i in temp:
    if U in i:
        print("Yes")
        exit()
print("No")

            
    
