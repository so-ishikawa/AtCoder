#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = set(input())
temp = set(list("abcdefghijklmnopqrstuvwxyz"))
print(list(temp-S)[0])
