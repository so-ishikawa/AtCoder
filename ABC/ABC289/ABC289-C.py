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
for i in range(M):
    c = int(input())
    temp = list(map(int, input().split()))
    a_list.append(temp)

counter = 0
import itertools

# x = 5
lis = []
for i in range(M):
    lis.append(i)
result = []
for n in range(1,len(lis)+1):
    temp_ = []
    for conb in itertools.combinations(lis, n):
        for i in conb:
            # print(conb)
            temp_ = temp_ + a_list[i]
        if len(set(temp_)) == N:
            counter += 1
        temp_ = []
print(counter)
        # result.append(list(conb)) #タプルをリスト型に変換
# print(result)
