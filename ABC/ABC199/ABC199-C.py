N = int(input())
S = input()
Q = int(input())


index_list = list(range(1, 2*N+1))
# print(index_list)
for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        # print("1 pre:", index_list)
        temp = index_list[a-1]
        index_list[a-1] = index_list[b-1]
        index_list[b-1] = temp
        # print("1 aft:", index_list)
        continue
    if t == 2:
        # print("2 pre:", index_list)
        for i in range(len(index_list)):
            if N > i:
                temp = index_list[i]
                index_list[i] = index_list[i+N]
                index_list[i+N] = temp
                
                
        # print("2 aft:", index_list)
        continue

dic = dict()
count = 1
for i in S:
    dic[count] = i
    count += 1

# print(dic, index_list)

for i in index_list:
    print(dic[i], end="")
