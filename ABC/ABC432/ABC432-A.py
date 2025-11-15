#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

temp_list = list(map(str,input().split()))
temp_list.sort(reverse=True)
print(int(temp_list[0]+temp_list[1]+temp_list[2]))
