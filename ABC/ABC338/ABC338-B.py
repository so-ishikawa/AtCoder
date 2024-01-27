from collections import defaultdict

S = input()

dic = defaultdict(lambda: 0)

for i in S:
    dic[i] = dic[i] + 1

temp = [kv for kv in dic.items() if kv[1] == max(dic.values())]
print((min(temp, key=lambda x:x[0]))[0])
