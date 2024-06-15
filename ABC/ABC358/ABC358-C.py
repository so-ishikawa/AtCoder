import itertools
N, M = map(int, input().split())
S_list = []
for i in range(N):
    S_list.append(input())

S_list_b = []
for i in range(N):
    temp = S_list[i]
    aa = ""
    for t in temp:
        if t == "o":
            aa += "1"
        else:
            aa += "0"
    S_list_b.append(int("0b"+aa, 2))

target = int(("0b" + "1"*M), 2)

for i in range(1, M+1):
    for v in itertools.combinations(S_list_b, i):
        xx = 0
        flag = True
        for x in v:
            # print(v)
            
            # xx = 0
            if flag:
                flag = False
                xx = x
                continue
            # print(xx, x)
            xx = xx | x
            # print(xx, "!")
        # print(v,xx, target)
        if xx == target:
            print(i)
            exit()
print("error!")
