from collections import defaultdict
dic = defaultdict(lambda: 0)

S = input()
for s in S:
    dic[s] += 1

for i in "ABCDEF":
    if i == "F":
        print(dic[i])
        exit()
    print(dic[i], end=" ")
