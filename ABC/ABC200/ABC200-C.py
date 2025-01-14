N = int(input())
A_list = list(map(int, input().split()))

def f(n):
    return((n-1)*n//2)

dic = dict()
for i in A_list:
    dic.setdefault(i%100, []).append(i)

temp = []
for k in dic.keys():
    rhs = []
    lhs = []
    for i in dic[k]:
        if i % 200 >= 100:
            rhs.append(i)
            continue
        lhs.append(i)
    temp.append(rhs)
    temp.append(lhs)

temp = [x for x in temp if len(x) != 0]
count = 0
for i in temp:
    count += f(len(i))

print(count)
