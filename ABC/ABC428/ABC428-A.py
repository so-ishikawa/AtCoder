#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S, A, B, X= map(int, input().split())

temp = 0
current = 0
while True:
    if current + A <= X:
        current += A
        temp += A*S
    else:
        # print((current+A-X), S,"!")
        temp += (X-current)*S
        break
    if current + B <= X:
        current += B
    else:
        break
    # print(current, temp)
print(temp)

    
