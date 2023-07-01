from decimal import Decimal

N = int(input())
A_list = []
B_list = []
for _ in range(N):
    a, b = map(int, input().split())
    A_list.append(a)
    B_list.append(b)

temp = [0] * N
for i in range(N):
    temp[i] = (i+1, float(A_list[i])/float(A_list[i]+B_list[i]))

temp.sort(key=lambda x: (-x[1], x[0]))
for i in temp:
    print(i[0], end=" ")
# print(temp)
