from collections import defaultdict
import math
S = input()
temp = "abcdefghijklmnopqrstuvwxyz"
dic = dict()# defaultdict(lambda: 0)

for t in temp:
    count = S.count(t)
    if count != 0:
        dic[t] = count

aa = [k for k in dic.keys() if dic[k] != 1]
if len(aa) == 0:
    print(len(S)*(len(S)-1)//2)
    exit()

temp2 = len(S)*(len(S)-1)//2
# print(temp2)
for k in dic.keys():
    n = dic[k] - 1
    xx = 0
    for i in range(n, 0, -1):
        xx += i
    n_ = xx
    # print(n_)
    temp2 -= n_
print(temp2 + 1)
