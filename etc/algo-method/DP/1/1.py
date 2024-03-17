N, X, Y = map(int, input().split())
pre_pre_value = X
pre_value = Y
temp = 0
for i in range(2, N):
    temp = (pre_pre_value + pre_value) % 100
    pre_pre_value = pre_value
    pre_value = temp
print(temp)
