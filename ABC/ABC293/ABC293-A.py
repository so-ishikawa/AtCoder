"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))
"""
S = input()
temp = []
for i in range(0, len(S),2):
    temp.append(S[i+1])
    temp.append(S[i])

print("".join(temp))
