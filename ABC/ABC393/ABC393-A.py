#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

S1, S2 = map(str, input().split())
if S1 == S2 == "fine":
    print(4)
    exit()
if S1 == "fine" and S2 == "sick":
    print(3)
    exit()
if S1 == "sick" and S2 == "fine":
    print(2)
    exit()
print(1)
