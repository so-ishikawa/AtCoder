#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
a_list = list(map(int, input().split()))

print(sum(a_list)%100)
