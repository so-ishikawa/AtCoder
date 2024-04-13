S = input()
dic = dict()
for s in S:
    if s in dic:
        dic[s] = dic[s] + 1
        continue
    dic[s] = 1

values = list(dic.values())

if len(S) == 1:
    print("No")
    exit()

for i in range(1, len(S)+10):
    # print(values)
    if values.count(i) == 0 or values.count(i) == 2:
        continue
    # print(values.count(i))
    print("No")
    exit()

print("Yes")
