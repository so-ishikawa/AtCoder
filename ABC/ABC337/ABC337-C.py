N = int(input())
A_list = list(map(int,input().split()))
dic = dict()
for i in range(1, len(A_list)+1):
    dic[A_list[i-1]] = i

start_num = A_list.index(-1) + 1
print(start_num, end=" ")

temp = start_num
for _ in range(len(dic)-1):
    print(dic[temp], end= " ")
    temp = dic[temp]


