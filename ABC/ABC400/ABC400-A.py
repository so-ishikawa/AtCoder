#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
A = int(input)

if 400 % A != 0:
    print(-1)
    exit()
print(int(400//A))
