N = int(input())
A_list = list(map(int, input().split()))
W_list = list(map(int, input().split()))

box_dic = dict()
for i in range(1, N+1):
    box_dic[i] = []

for index in range(N):
    box_dic[A_list[index]].append(W_list[index])
# print(box_dic)
sum_value = 0
for i in box_dic.values():
    if len(i) == 0 or len(i) == 1:
        continue
    #temp = set(i)
    i.remove(max(i))
    sum_value += sum(i)

print(sum_value)
