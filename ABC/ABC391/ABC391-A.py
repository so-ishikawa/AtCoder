#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
D = input()
dic = dict({"N":"S",
            "E":"W",
            "W":"E",
            "S":"N",
            "NE":"SW",
            "SW":"NE",
            "NW":"SE",
            "SE":"NW"})
print(dic[D])
