#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math
A, B = map(int, input().split())

temp = A / B
up = math.ceil(temp)
down = int(temp)

up_diff = abs(temp-up)
down_diff = abs(temp-down)
if up_diff < down_diff:
    print(up)
    exit()
print(down)
