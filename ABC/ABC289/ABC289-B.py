"""
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))

"""
N, M = map(int, input().split())
a_list = []
if M != 0:
    a_list = list(map(int, input().split()))

#dummy
a_list.insert(0, "dummy")

temp = []
pre_flag = False
already_print_flag = False
for i in range(N+1):
    # print(i,"!")
    if i == 0:
        continue
    if i in a_list:
        temp.append(i)
        pre_flag = True
        continue
    if pre_flag:
        temp.append(i)
        pre_flag = False
        already_print_flag = True
    if len(temp) != 0:
        # print(temp,"!")
        temp.reverse()
        for j in temp:
            print(j, end=" ")
        temp.clear()
    if already_print_flag:
        already_print_flag = False
        continue
    print(i, end=" ")



