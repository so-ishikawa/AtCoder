#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

S = input()
T = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"
result = T.find(S)

if result == 0:
    print("Do")
elif result == 2:
    print("Re")
elif result == 4:
    print("Mi")
elif result == 5:
    print("Fa")
elif result == 7:
    print("So")
elif result == 9:
    print("La")
elif result == 11:
    print("Si")
else:
    raise

