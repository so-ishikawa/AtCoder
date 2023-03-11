"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))
"""
N = int(input())
a_list = list(map(int, input().split()))

all_set = set(range(1, N+1))
temp_set = set()

for i in range(len(a_list)):
    if (i + 1) not in temp_set:
        temp_set.add(a_list[i])

x = list(all_set - temp_set)
x.sort()
print(len(x))
for i in x:
    print(i, end=" ")
