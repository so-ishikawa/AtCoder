X = input()
N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

dic = dict()
for i in range(len(X)):
    dic[X[i]] = i

result = []
for s in S_list:
    temp = []
    for i in s:
        temp.append(dic[i])
    temp = tuple(temp)
    result.append((temp, s))

result.sort(key=lambda x: x[0])

for i in result:
    print(i[1])
