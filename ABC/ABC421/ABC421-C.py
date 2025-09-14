#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
S = input()

dic = dict()
count = 0
for i in range(2*N):
    if S[i] == "A":
        dic[count] = i
        count += 1
temp = 0
for i in range(N):
    # print(temp)
    temp += abs(dic[i] - i*2) 

temp_ = 0
for i in range(N):
    temp_ += abs(dic[i] - (i*2+1))
print(min(temp,temp_))
