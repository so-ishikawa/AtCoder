#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
X = int(input())
temp = list(str(X))

num_0 = temp.count("0")
except_0_list = [int(x) for x in temp if x != "0"]
except_0_list.sort()
except_0_list = [str(x) for x in except_0_list]
aa = str(except_0_list[0]) + "0"*num_0 + ("".join(except_0_list)[1:])
print(aa)
