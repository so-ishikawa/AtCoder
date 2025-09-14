#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
X, C = map(int, input().split())

temp = X*1000/(1000+C)
temp = (temp // 1000)*1000
print(int(temp))
