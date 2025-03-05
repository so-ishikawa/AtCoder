#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, K = map(int, input().split())

print(min(abs((N % K)-K), abs(N%K)))
