#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, K = map(int, input().split())

num = 2**N

amari = K % num
# print(amari,"!")
ans = K // num
temp = amari
if amari > num // 2:
    amari = (num //2) - (amari % (num//2) )

print(amari)
for i in range(num):
    if temp + i < num:
        print(ans, end=" ")
        continue
    print(ans + 1, end=" ")
