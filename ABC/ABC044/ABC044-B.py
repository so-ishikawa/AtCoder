w_list = list(input())
dic = dict()

for w in w_list:
    if w not in dic:
        dic[w] = 1
    else:
        dic[w] = dic[w] + 1

if len([x for x in dic.values() if x % 2 == 1]) != 0:
    print("No")
    exit()

print("Yes")
