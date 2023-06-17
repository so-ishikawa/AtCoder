N = int(input())
A_list = list(map(int, input().split()))

dic = dict()
for i in range(len(A_list)):
    if A_list[i] not in dic:
        dic[A_list[i]] = -1
        continue
    if A_list[i] in dic and dic[A_list[i]] == -1:
        dic[A_list[i]] = i
        continue
    
dic2 = sorted(dic.items(), key=lambda x:x[1])
for i in dic2:
    print(i[0], end=" ")
