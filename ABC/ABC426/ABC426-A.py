#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
X, Y = map(str,  input().split())
dic = dict({"Ocelot":3, "Serval":2, "Lynx":1})

if dic[X] <= dic[Y]:
    print("Yes")
    exit()
print("No")
