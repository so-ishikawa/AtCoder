N = int(input())
dic = dict()
for i in range(N):
    f, s = map(int, input().split())
    if f in dic:
        dic[f].append(s)
        continue
    dic[f] = [s]
# print(dic)
max_value = 0
# same
for _key in dic.keys():
    temp = dic[_key]
    if len(temp) < 2:
        continue
    # print(temp)
    temp.sort(reverse=True)
    a = temp[0] + temp[1]//2
    if max_value < a:
        max_value = a
    
#diff
b = []
for _key in dic.keys():
    b.append(max(dic[_key]))

b.sort(reverse=True)
diff_best = 0
if len(b) >= 2:
    diff_best = b[0] + b[1]
print(max(max_value, diff_best))
