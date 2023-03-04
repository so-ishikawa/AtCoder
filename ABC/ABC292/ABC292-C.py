"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

l = list(map(int, input().split()))
"""
N = int(input())

temp = [0] * (N + 1)
temp[2] = 1
temp[3] = 4
temp[4] = 8
for i in range(N + 1):
    if i <= 4:
        continue
    temp[i] = 4 * int(temp[i-2] / 4 + temp[i-1] /4)
print(temp[N])
