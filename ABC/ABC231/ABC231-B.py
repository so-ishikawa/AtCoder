N = int(input())
S_list = []
for _ in range(N):
    S_list.append(input())

dic = dict()
for i in S_list:
    if i in dic:
        dic[i] = dic[i] + 1
        continue
    dic[i] = 1

print(max(dic, key=dic.get))

