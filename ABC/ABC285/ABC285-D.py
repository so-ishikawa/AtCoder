N = int(input())
list_S = []
list_T = []
for i in range(N):
    s,t = input().split()
    #t = input()
    list_S.append(s)
    list_T.append(t)

dic = {}
for i in range(N):
    dic[list_S[i]] = list_T[i]
# set_T = set(list_T)


flag = True
for i in range(N):

    if dic[list_S[i]] not in dic:
        continue

    source = list_S[i]
    temp = []

    while True:

        if dic[source] not in dic:
            break

        if source in temp:
            flag = False
            break

        temp.append(source)
        source = dic[source]
        if source in temp:
            flag = False
            break

    if not flag:
        break

if flag:
    print("Yes")
else:
    print("No")
