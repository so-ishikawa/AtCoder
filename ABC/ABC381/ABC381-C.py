N = int(input())
S = input()

import re

result = re.findall("[1]*\/[2]*",S)
__max = 0
for _max in result:
    temp = min(_max.count("1"), _max.count("2"))*2 + 1
    if temp > __max:
        __max = temp
print(__max)
